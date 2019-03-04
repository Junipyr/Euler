import itertools
import sympy


for i in range(4, 10):
  perms = list(itertools.permutations(j for j in range(1, i)))
  for p in perms:
    if p[len(p) - 1] not in [2, 4, 5, 6, 8]:
      n = int("".join(str(d) for d in p))
      if sympy.isprime(n):
        ans = n

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr