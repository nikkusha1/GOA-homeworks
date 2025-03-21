//2
class Computer {
    constructor(brand, cpu, ram, storage) {
        this.brand = brand;
        this.cpu = cpu;
        this.ram = ram;
        this.storage = storage;
    }

    info() {
        return `Computer: ${this.brand}, CPU: ${this.cpu}, RAM: ${this.ram}GB, Storage: ${this.storage}GB`;
    }
}

const pc = new Computer("Dell", "Intel i7", 16, 512);
console.log(pc.info());
//2
class Keyboard {
    constructor(brand, keys, isWireless) {
        this.brand = brand;
        this.keys = keys;
        this.isWireless = isWireless;
    }

    info() {
        return `Keyboard: ${this.brand}, Keys: ${this.keys}, Wireless: ${this.isWireless}`;
    }
}

const kb = new Keyboard("Logitech", 104, true);
console.log(kb.info());
//3
//კონსტრუქტორი არის სპეციალური მეთოდი, რომელიც იძახება კლასის ობიექტის შექმნისას.

//4
const arr1 = [1, 2, 3, 4, 5];
const arr2 = ["a", "b", "c"];
const arr3 = [true, false, true];

for (let num of arr1) {
    console.log(num);
}

for (let char of arr2) {
    console.log(char);
}

for (let value of arr3) {
    console.log(value);
}
