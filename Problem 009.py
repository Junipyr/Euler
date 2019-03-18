def pythag_triple(n):
  for a in range(1, n // 2):
    b = (n**2/2 - n*a)/(n - a)
    if b.is_integer():
      return int(a*b*(n - a - b))
  return None

print(pythag_triple(1000))


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr