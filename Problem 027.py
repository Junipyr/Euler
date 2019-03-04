# From n = 0, b must be prime. Hence, from n = 1, a must be odd.

import sympy


a_max = b_max = 1000
max_n = 0
primes = set(sympy.sieve.primerange(1, 80**2 + 80*a_max + b_max))
b_set = set(p for p in primes if p < b_max)

for a in range(-a_max + 1, a_max, 2):
  for b in b_set:
    n = 0
    while n**2 + a*n + b in primes:
      n += 1
    if n > max_n:
      max_n = n
      ans = a * b

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr