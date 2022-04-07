#GoshaGui beta 1.0
#Модули:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ui
import eel
#Распознание голоса
import speech_recognition as sr
#Голос бота
import pyttsx3
#Время
from datetime import datetime
#Json
import json
# os
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
#Музыка
import pygame as pg
#Время
import time as t
#Рандом для некоторых функций
import random
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

eel.init("Web")
pg.mixer.init()

#Голос, НЕ ТРОГАТЬ(ЕСЛИ НЕ РАЗБИРАЕШЬСЯ)!!!----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Aleksandr':
        engine.setProperty('voice', voice.id)

#Список действий и другое...------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Список комманд
help_list = "Время\nПомощь\nПогода\nДокументация\nУправление файлами\nШутки\nПереводчик"

#Словарь обращений
with open("vocabulary.json", "r", encoding="UTF=8") as read_file: 
    b_voc = json.load(read_file)

# Звуки
sound_click = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + "\\web\\data\\Sounds\\2.wav")
sound_start = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + "\\web\\data\\Sounds\\1.wav")

#Шутки
joke1 = ["Я не знаю шуток! ха-ха!",  "Знаешь почему курица перешла дорогу? Потому что она умеет ходить! ха-ха!", "Россия - страна непойманных воров и вечно будущего счастья...", "Если вдоль зебры лежат полицейские, значит, охота не удалась.","Детство - это когда кот старше тебя.","Идея тонкого комплимента: 'Маска тебе к лицу!'","Очень боюсь, что хакеры сольют в сеть мои интимные фото. И они никому не понравятся."]

#Функции------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Распознавание голоса
def voice():
    global what
    try:
        r = sr.Recognizer()

        with sr.Microphone(device_index=3) as source:
            audio = r.listen(source)

        what = r.recognize_google(audio, language = "ru-RU").lower()
    except:
        speak("Извини, но у тебя проблемы с микрофоном")

#Синтез речи
def speak(what):
    engine.say( what )
    engine.runAndWait()
    engine.stop()

#Время
def time():
    now = datetime.now()
    speak("Сейчас: " + str(now.hour) + ":" + str(now.minute))
    
#Шутки
def joke():
	ask_joke = random.choice(joke1)
	speak(ask_joke)
	joke_pl = pg.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + "\\web\\data\\Sounds\\joke.wav")
	joke_pl.play()
	t.sleep(3)

#Помощь
def help():
	speak("Список комманд: ")
	speak(help_list)

#Стартовый звук
sound_start.play()

#Основной цикл функций---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@eel.expose
#Распознавание голоса
def main():
    #Звук кнопки
    sound_click.play()
    t.sleep(1)
    #Голос
    voice()

    #Время
    if what in b_voc["time"]:
        time()
        return what
    
    #Шутка
    elif what in b_voc["jokes"]:
        joke()
        return what
    
    #Помощь
    elif what in b_voc["help"]:
        help()
        return what
    
    #Ни одна комманда не сработала
    else:
        speak("Я тебя не понял, что-то не так в твоем вопросе")
        return what

#Start программы
eel.start("index.html", size=(500,700))