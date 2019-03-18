import sympy


ans = count = 0
exceptions = ["2", "4", "5", "6", "8"]
primes = set(sympy.sieve.primerange(0, 1000000))

for p in primes:
  u = v = str(p)
  if any(n in u for n in exceptions) and p > 99:
    continue
  while len(u) > 0:
    if int(u) not in primes or int(v) not in primes:
      break
    u, v = u[1:], v[:len(v) - 1]
  if len(u) == 0 and p > 10:
    count += 1
    ans += p
    if count == 11: # There are eleven truncatable primes
      break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr