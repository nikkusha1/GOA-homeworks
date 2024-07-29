# task 1
counter= 1
while counter <= 100:
    if counter > 60:
        print(counter)
    elif counter < 50:
        print(counter)
    counter = counter + 1


# task 2
sum_of_numbers = 0
current_number = 1
while sum_of_numbers < 50:
    sum_of_numbers += current_number
    current_number = current_number + 1
print(sum_of_numbers)



# task 3
number = int(input("Enter number: "))
if number % 2 == 0:
    print("number is even.")
else:
    print("number is odd.")


# task 4
grade = int(input("Enter your grade: "))
if 90 <= grade <= 100:
    print("Grade A")
elif 80 <= grade <= 89:
    print("Grade B")
elif 70 <= grade <= 79:
    print("Grade C")
elif 60 <= grade <= 69:
    print("Grade D")
elif 0 <= grade <= 59:
    print("Grade F")
else:("grade is false")

# task 5
age = int(input("Enter your age: "))
if age < 13:
    print("You are  kid")
elif 13 < age < 20:
    print("You are  teenager")
else:
    print("You are grown up")

