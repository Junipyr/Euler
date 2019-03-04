import sympy


primes = set(sympy.sieve.primerange(1, 10000))

for n in range(3, 10000, 2):
  if n not in primes and not any(n - 2*i*i in primes for i in range(1, 100)):
    ans = n
    break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr