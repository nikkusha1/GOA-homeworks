
def print_range(start, end):          #task 2
    for number in range(start, end):
        print(number)
print_range(15, 20)


def introduce(name, surname, age, academy):         #task 3
    print(f"My name is {name}, my surname is {surname}, I study in {academy}.")
introduce("nika", "giorgadze", 15, "GOA academy")


def greet(name, surname):         #task 4
    print(f"Hello, {name} {surname}!")
greet("Nika","Giorgadze")



def numbers(a, b):     #task 5
    return a + b
result = numbers(10, 5)
print(result)

def three_numbers(a, b, c):      #task 6
    return a * b * c
result = three_numbers(10, 2, 4)
print(result)


def foods(foods):         #task 7
    for food in foods:
        print(food)
food_list = ["Khachapuri", "Khinkali", "pizza", "Qababi", "Salad", "Mtsvadi"]
foods(food_list)



















