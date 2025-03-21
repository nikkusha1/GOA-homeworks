let score = parseInt(prompt("Enter your score:"));
if (score >= 90 && score <= 100) {
    console.log("Grade A");
} else if (score >= 80 && score <= 89) {
    console.log("Grade B");
} else if (score >= 70 && score <= 79) {
    console.log("Grade C");
} else if (score >= 60 && score <= 69) {
    console.log("Grade D");
} else {
    console.log("Grade F");
}

let age = parseInt(prompt("Enter your age:"));
if (age < 13) {
    console.log("You are kid");
} else if (age < 18) {
    console.log("You are not adult yet");
} else {
    console.log("You are adult");
}

let num = 5;
while (num <= 20) {
    console.log(num);
    num ++;
}

for (let i = 0; i <=100; i++) {
    console.log(i);
}

for (let i = 50; i <= 100; i += 2) {
    console.log (i);
}