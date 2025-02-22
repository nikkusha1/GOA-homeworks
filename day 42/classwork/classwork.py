#1
def create_array(n):
    res=[]
    for i in range(1, n + 1):
        res.append(i)
    return res
#2
def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

def divisible_by(numbers, divisor):
    return [ num for num in numbers if num % divisor == 0]
#3
geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
#4
def get_real_floor(n):
    # code here
    if n <= 0:
        return n 
    if n < 13:
        return n - 1
    return n - 2
#4
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
#5
def friend(x):
    return [name for name in x if len(name) == 4]
#6
def maskify(cc):
    return '#' * max(len(cc) - 4, 0) + cc[-4:]
#7
def longest(a1, a2):
    return ''. join(sorted(set(a1 + a2)))
