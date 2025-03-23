function changeText() {
    document.getElementById("text").textContent = "who are you?";
}

function increaseFontSize() {
    let text = document.getElementById("text");
    let currentSize = window.getComputedStyle(text).fontSize;
    text.style.fontSize = (parseInt(currentSize) + 2) + "px";
}



let array = [1, 2, 3, 4, 5];
let firstElement = array.shift();
let lastElement = array.pop();
console.log(firstElement);
console.log(lastElement);