// GoshaGui beta 1.0

// Переменные


// Function
// Распознавание голоса и вывод на экран
document.querySelector(".Gosha").onclick = function () {  
    eel.main()(function(letter){                      
        document.querySelector(".text__recog").innerHTML = letter;
    })
}