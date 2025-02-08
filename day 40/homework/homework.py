#1
def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'
#2
def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b
#3
def fix_the_meerkat(arr):
   return arr[::-1]
#4
def find_multiples(integer, limit):
 return [i for i in range(integer, limit + 1, integer)]
#5
# a == "code"
# b == "wa.rs"
# name == a + b
# name = "codewa.rs"