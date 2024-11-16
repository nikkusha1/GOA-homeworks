numbers = [x for x in range(1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i % 2 == 0]
print(numbers)

names = ["nika", "saba", "goga", "aleksandre"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

number = [i**2 for i in range(1, 11)]
print(number)
