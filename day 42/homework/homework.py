#1
def open_or_senior(data):
     return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

#2
def row_sum_odd_numbers(n):
    return n ** 3

#3
def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug  
        t += 1
    return t

#4
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))