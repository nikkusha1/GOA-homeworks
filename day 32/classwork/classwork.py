# 1
sum_numbers = lambda x, y: x + y
print(sum_numbers(20, 5)) 


# 2
double_number = lambda x: x * 2
print(double_number(10))  


# 4
numbers = [1, 3, 6, 2, 9]
double_numbers = list(map(lambda x: x * 3, numbers))
print(double_numbers)

# MAPS
#1
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares) 

#2
celsius = [0, 20, 30, 40]
l = list(map(lambda x: x * 9/5 + 32, celsius))
print(celsius) 

#3
words = ["hello", "world", "python"]
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)


# FILTERS
#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#2

#3
numbers = [3, 9, 15, 22, 27, 30]
divide_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divide_3)

