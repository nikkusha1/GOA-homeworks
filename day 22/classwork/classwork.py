#1
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
#2
def get_middle(s):
    pass
    return s[(len(s)-1)//2 : len(s)//2+1]
#3
def to_jaden_case(string):
    # ...
     return ' '.join([word.capitalize() for word in string.split()])