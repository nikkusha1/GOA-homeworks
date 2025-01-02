#2
numbers = [2, 4, 6, 8, 10]
double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers) 

#3
names = ["Alice", "Bob", "Charlie"]
hello = list(map(lambda name: f"Hello, {name}", names))
print(hello) 

#4
words = ["apple", "banana", "kiwi"]
lenghts= list(map(len, words))
print(lenghts) 

#5
numbers = [-5, 3, -2, 7, 0, 10]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)

#6
words = ["pear", "apple", "peach", "grape"]
p = list(filter(lambda word: word.startswith('p'), words))
print(p) 

#7
numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50) 

#8
# map: გამოიყენება კოლექციის თითოეულ ელემენტზე ოპერაციის შესასრულებლად ანუ ყველა ელემენტის შესაცვლელად.
# filter: გამოიყენება კოლექციის ელემენტების გასაფილტრად.





