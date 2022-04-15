// GoshaGui beta 1.0

// Переменные
let settings = document.getElementById("settings");
let settingsBtn = document.getElementById("Sett_Btn");
let speakLight = document.getElementById("sp");
let InpText = document.getElementById("inp2");
let cont = document.getElementById("cont2");

let countSett = 1;

// Function
// Распознавание голоса и вывод на экран
document.getElementById("Gosha").addEventListener("click", function () {  
    document.getElementById("Gosha").classList.remove("fade-in");
    document.getElementById("Gosha").offsetWidth = document.getElementById("Gosha").offsetWidth;
    document.getElementById("Gosha").classList.add("fade-in");

    speakLight.style.opacity = "1";
    speakLight.style.animation = "spanim 1s infinite";

    eel.main()(function(letter){
        speakLight.style.animation = "none";
        speakLight.style.opacity = "0";
        document.querySelector(".text__recog").innerHTML = letter;
        eel.findweather()(function(listweather) {
            if (String(listweather).includes(letter)) {
                cont.style.opacity = "1";
            }
        });
    });
});

// Настройки
settingsBtn.addEventListener("click", function () {
    if (countSett == 0) {
        settings.style.opacity = "0";
        countSett += 1;
    } else {
        settings.style.opacity = "1";
        countSett -= 1;
    }
});

// Погода
function EnterData(){
    cont.style.opacity = "0";
    eel.weather(InpText.value)();
}

// Изменение настроек
function ChangeSett() {
    let value = document.querySelector(".inp").value;
    eel.changesett(value)(function(){                      
        alert("Изменено :)")
        alert("Требуется перезапуск программы!")
    });
}

function PrintMicr1() {
    eel.PrintMicr()(function(MicrList){
        alert(MicrList);
    });
}

// faq
function faq() {
    eel.faq()();
} 