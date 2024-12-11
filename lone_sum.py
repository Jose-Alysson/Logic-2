'''Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0'''

def lone_sum(a, b, c):
  if a != c and a != b:
    if c == b:
      return a
    if b != c:
      return a + b + c
  else:
    if a == b and b == c:
      return 0
    if a == c:
      return b
    if b == c:
      return a
    if a == b:
      return c


print(lone_sum[10, 9, 4])
