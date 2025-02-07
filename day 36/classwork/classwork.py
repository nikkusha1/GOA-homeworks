#1
def goals(laLiga, copaDelRey, championsLeague):
    
 return laLiga+copaDelRey+championsLeague

#2
def double_char(s):
    result = ""
    for c in s:
        result += c * 2
    return result
#3
def get_age(age):
    #your code here
    return int(age[0])
#4
def feast(beast, dish):
     return beast[0] == dish[0] and beast[-1] == dish[-1]

#5
def array_plus_array(arr1,arr2):
 return sum(arr1) + sum(arr2)