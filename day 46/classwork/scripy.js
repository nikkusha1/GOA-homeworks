function changeButton(button, color, text) {
    button.style.backgroundColor = color;
    button.textContent = text;
}

document.getElementById("btn1").addEventListener("click", function() {
    changeButton(this, "yellow", "Clicked 1");
});

document.getElementById("btn2").addEventListener("click", function() {
    changeButton(this, "green", "Clicked 2");
});

document.getElementById("btn3").addEventListener("click", function() {
    changeButton(this, "orange", "Clicked 3");
});


function changeText1() {
    let button = document.getElementById("btn1");
    button.innerHTML = "Clicked Button 1";
    button.style.fontSize = "20px";
}

function changeText2() {
    let button = document.getElementById("btn2");
    button.innerHTML = "Clicked Button 2";
    button.style.fontSize = "20px";
}


function changeText1() {
    let button = document.getElementById("btn1");
    button.innerHTML = "Clicked Button 1";
    button.style.fontSize = "20px";
}

function changeText2() {
    let button = document.getElementById("btn2");
    button.innerHTML = "Clicked Button 2";
    button.style.fontSize = "20px";
}


let fruits = ["orange", "peach", "banana"]
fruits.unshift("peach");
console.log(fruits);

let cars = ["BMW", "opel", "Mercedes"];
cars[cars.length - 1] = "Audi";
console.log(cars);


let items = ["TV", "Phone", "ipad", "microphone"];
items.shift();
items.pop(); 
console.log(items);