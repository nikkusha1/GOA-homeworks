def hello_world():          #1
    return "Hello world!"
print(hello_world())


def greet_by_name(name):     #2
    print(f"Hello, {name}!")

greet_by_name(input("enter yout name: "))


def numbers(num1, num2):    #3
    return num1 * num2
result = numbers(3, 4)
print(result) 

def sum_of_three_numbers(num1, num2, num3):   #4
    return num1 + num2 + num3
result = sum_of_three_numbers(2, 5, 10)
print(result) 


def adult(age):   #5
    if age >= 18:
        return "adult"
    else:
        return "Not an adult"
result = adult(20)
print(result) 







