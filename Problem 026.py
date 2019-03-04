# We want to find the largest full repetend prime below 1000.

import sympy


def cycle_length(n):
  a = 1
  while (10**a) % n != 1:
    a += 1
  return a

for n in range(1000, 1, -1):
  if sympy.isprime(n) and cycle_length(n) == n - 1:
    ans = n
    break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr