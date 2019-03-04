import sympy


ans = count = 0
exceptions = ["2", "4", "5", "6", "8"]
primes = set(sympy.sieve.primerange(0, 1000000))

for p in primes:
  s1 = s2 = str(p)
  if any(n in s1 for n in exceptions) and p > 99:
    continue
  while len(s1) > 0:
    if int(s1) not in primes or int(s2) not in primes:
      break
    s1, s2 = s1[1:], s2[:len(s2) - 1]
  if len(s1) == 0 and p > 10:
    count += 1
    ans += p
    if count == 11: # There are eleven truncatable primes
      break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr