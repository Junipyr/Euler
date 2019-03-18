def prod_palindrome(n, lbound=0):
  prods = []
  for i in range(n, lbound, -1):
    if i % 10 != 0:
      for j in range(n, max(i, n + lbound - i) - 1, -1):
        if j % 10 != 0:
          ij = str(i * j)
          if ij == ij[: : -1]:
            lbound = max(lbound, i + j - n)
            prods.append(i * j)
  return max(prods)

print(prod_palindrome(1000))


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr