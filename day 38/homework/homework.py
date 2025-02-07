#2
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i + 1]
    return None

#3
def to_alternating_case(string):
    return "".join(c.lower() if c.isupper() else c.upper() for c in string)

#4
def correct(s):
     return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')
#5
def bonus_time(salary, bonus):
      return f"${salary * 10 if bonus else salary}"




