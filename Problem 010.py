import sympy

maxPrime = 2000000

ans = sum(sympy.sieve.primerange(0, maxPrime))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr