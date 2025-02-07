#1
def rental_car_cost(d):
      return d * 40 - (50 if d >= 7 else 20 if d >= 3 else 0)
#2
def quarter_of(month):
     return (month + 2) // 3
#3
def remove_exclamation_marks(s):
      return s.replace('!', '') 
#4
def points(games):
  return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, game.split(':')) for game in games))
#5
def get_volume_of_cuboid(length, width, height):
    return length * width * height
#6
def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot
#7
def other_angle(a, b):
 return 180 - (a + b)
#8
def set_alarm(employed, vacation):
       return employed and not vacation
#9
def sum_mix(arr):
     return sum(int(i) for i in arr)
#10
def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    return sum(arr) - min(arr) - max(arr)