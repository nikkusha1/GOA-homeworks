#3
def sum_numbers(numbers):
    return sum([int(num) if isinstance(num, int) else int(num) for num in numbers])

print(sum_numbers([10, "10"]))  
print(sum_numbers([5, "15", 20, "25"]))  

#2
# try:
#     print(undeclared_variable)  
# except NameError:
#     print("Variable is not defined")

#     try:
#     my_list = [1, 6, 4]
#     print(my_list[5])  
# except IndexError:
#     print("Index out of range")

#     try:
#     num = int("hello")  
# except ValueError:
#     print("Invalid value for conversion")