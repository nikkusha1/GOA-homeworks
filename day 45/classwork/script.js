let car1 = {
    brand: "Audi",
    model: "A4",
    year: 2023
  };
  
  let car2 = {
    brand: "Mercedes",
    model: "E-class",
    year: 2024
  };
  
  let car3 = {
    brand: "BMW",
    model: "5 series",
    year: 2022
  };

  function Car(brand, year, model, horsePower) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.horsePower = horsePower;

    this.increaseHorsePower = function() {
      this.horsePower += 50;
    };
  }

  let myCar = new Car("mercedes", "cls", 2022, 300);

  console.log(myCar.horsePower);
  myCar.increaseHorsePower();
  console.log(myCar.horsePower);


  let myArray1 = [1, 2, 3, 4, 5];
console.log(myArray1);

let myArray2 = new Array(1, 2, 3, 4, 5);
console.log(myArray2);

//indexing
console.log(myArray1[0]); 
console.log(myArray2[4]); 

//siciling
let slicedArray1 = myArray1.slice(1, 4);
console.log(slicedArray1); 

// Associative arrays ეს არის ისეთი array, სადაც რიცხვების ნაცვლად იყენებ სიტყვებს.
// array-ები მუშაობენ რიცხვებით, ხოლო associative arrays-ს უნდა ჰქონდეს სიტყვები
// let myArray1 = [1, 2, 3, 4, 5];

for (let i = 0; i < myArray1.length; i++) {
  console.log(myArray1[i]);
}
