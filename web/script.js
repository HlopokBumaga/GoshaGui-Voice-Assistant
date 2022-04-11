// GoshaGui beta 1.0

// Переменные
let settings = document.getElementById("settings");
let settingsBtn = document.getElementById("Sett_Btn");

let countSett = 1;

// const json1 = readFileSync('config.json', 'utf8');

// Function
// Распознавание голоса и вывод на экран
document.getElementById("Gosha").addEventListener("click", function () {  
    document.getElementById("Gosha").classList.remove("fade-in");
    document.getElementById("Gosha").offsetWidth = document.getElementById("Gosha").offsetWidth;
    document.getElementById("Gosha").classList.add("fade-in");
    eel.main()(function(letter){                      
        document.querySelector(".text__recog").innerHTML = letter;
    });
})

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