#1
def str_count(strng, letter):
    return strng.count(letter)
#2
def is_even(n): 
    return (n, int) and n % 2 == 0
#3
def get_planet_name(id):
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name
#4
def move(position, roll):
    return position + roll * 2
#5
def enough(cap, on, wait):
    return max(0, on + wait - cap)
#6
def between(a,b):
    return list(range(a, b + 1))
#7
def say_hello(name):
  return f"Hello, {name}"
#8
def is_uppercase(inp):
    return inp == inp.upper()
#9
def monkey_count(n):
 return list(range(1, n + 1))
#10
def powers_of_two(n):
 return [2**i for i in range(n + 1)]