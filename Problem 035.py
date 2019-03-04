import sympy


def rotate(n):
  last = n % 10
  pwr = len(str(n)) - 1
  n //= 10
  return n + last * 10**pwr

ans = 0
primes = set(sympy.sieve.primerange(1, 1000000))

for p in primes:
  q = rotate(p)
  is_circular = True
  while q != p:
    if q not in primes:
      is_circular = False
      break
    q = rotate(q)
  if is_circular:
    ans += 1

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr