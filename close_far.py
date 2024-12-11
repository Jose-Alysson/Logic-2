'''Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False'''

def close_far(a, b, c):
  farB = abs(b - a) >= 2
  farC = abs(c - a) >= 2
  farBC = abs(b - c) >= 2

  closeB = abs(b - a) <= 1
  closeC = abs(c - a) <= 1

  if farB == True and farC == True or closeB == True and closeC == True:
    return False
  if closeB == True and farC == True and farBC == True:
    return True
  if closeC == True and farB == True and farBC == True:
      return True
  else:
    return False
