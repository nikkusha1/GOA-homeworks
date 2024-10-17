#manual sum
def manual_sum(sum1):
    result = 0
    for i in sum1:
        result += i
    return result
print(manual_sum([1, 2, 4, 0, -1]))

#manual len
def manual_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count
print(manual_len([1, 2, 3, 4, 5]))

#manual min
def manual_min(arr):
    if not arr:
        return None
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum
print(manual_min([1, 4, 6, 8, 9])) 