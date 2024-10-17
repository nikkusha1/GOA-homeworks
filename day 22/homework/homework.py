# manual_max
def manual_max(range):
    max_value = range[0]
    for i in range[1:]:
        if i > max_value:
            max_value = i
    return max_value

# manual_replace
def manual_replace(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst

# manual_append
def manual_append(lst, value):
    lst += [value]  
    return lst


