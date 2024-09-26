# task 2
a = 5
b = 10
sum_ab = a + b
print(sum_ab)

#task 3
str1 = "Hello"  #კონკატენაცია არის ორი ან მეტი სტრიქონის ერთმანეთში შერწყმა/შეერთება.
str2 = "World"
concatenated = f"{str1} {str2}"
print(concatenated)

#task 4
a = 10     #ეს არის implicit conversion
b = 2
quotient = a / b
print(quotient)

#task 5
a = 5
b = 5
print(a == b) 

a = 5
b = 3
print(a != b)  

a = 7
b = 3
print(a > b) 

a = 2
b = 4
print(a < b) 

a = 5
b = 5
print(a >= b) 

a = 3
b = 5
print(a <= b) 

#task 6
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

#task 7
print(4 + 4 == 8)
print(10 - 3 != 6) 
print(10 * 5 > 10)
print(21 / 3 < 6)
print(8 + 5 >= 12)
print(10 - 2 <= 7)
print(5 * 5 == 25)
print(10 / 2 != 9)

#task 8
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

#task 9
print((10 + 5 == 15) and (3 * 3 > 7))
print((10 - 2 != 6) or (3 * 7 == 21))
print((10 / 2 < 6) and (4 + 1 <= 5))
print(not (10 + 2 == 13))
print((6 / 2 == 4) or (6 - 2 < 2))

#task 10
for i in range(1, 11):
    print(i)

#task 11
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for i in numbers:
    total_sum += i
print(total_sum)

#task 12
text = "Hello, World!"
for i in text:
    print(i)

#task 13
number = 1
while number <= 10:
    print(number)
    number = number + 1

#task 14
number = 1
while number <= 100:
    if 51 <= number <= 59:
        number += 1
    print(number)
    number += 1

#task 15
sum = 0 
num = 1 

while sum < 50:
    sum += num  
    num += 1   

print(f"{sum},{num - 1}")



#task 16
def check_divisibility():
    number = int(input("Enter number: "))
    
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} It is divisible by both 3 and 5.")
    elif number % 3 == 0:
        print(f"{number} divisible by 3.")
    elif number % 5 == 0:
        print(f"{number} divisible by 5.")
    else:
        print(f"{number} It is not divisible by 3 or 5.")
        
check_divisibility()

#task 17
def calculate_average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num  
        count += 1    
    
    if count == 0:
        return 0  
    
    return total / count 

numbers = [1, 3, 4, 5, 2]
output = calculate_average(numbers)
print(output)

#task 18
def func1(str1):
    res = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            res += str1[i].upper()
        else:
            res+= str1[i]
            return res
        print(func1("hello"))


#task 19
def square_numbers(numbers):
    squared_list = []

    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list
test_list = [3, 12, 5, 2, 6]
print(square_numbers(test_list))






































