numbers = [1, 2, 3, 4]
squared = list(manual_map(lambda x: x ** 2, numbers))
print(squared)  

numbers = [1, 2, 3, 4]
even_numbers = list(manual_filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)