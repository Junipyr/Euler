import sympy


primes = set(sympy.sieve.primerange(1000, 10000))

for p in primes:
  q, r = p + 3330, p + 6660
  if q in primes and r in primes and p != 1487:
    if set(str(q)) == set(str(r)) == set(str(p)):
      ans = int(str(p) + str(q) + str(r))
      break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr