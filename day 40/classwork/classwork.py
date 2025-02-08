#
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

#
def final_grade(exam, projects):
  if exam > 90 or  projects > 10: return 100
  if exam > 75 and projects >= 5: return 90
  if exam > 50 and projects >= 2: return 75
  return 0

#
def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))
#
def sum_str(a, b):
       return str(int(a or 0) + int(b or 0))
#
def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]
#
def reverse_list(l):
  return l[::-1]
#
def odd_count(n):
 return (n - 1) // 2
#
def find_difference(a, b):
     return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])
#
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
#
def two_sort(lst):
    return '***'.join(min(lst))