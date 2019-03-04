import math


lim = 28124
abts = set()
ans = 0

def is_abundant(n):
  rt = math.sqrt(n)
  s = sum(i + n//i for i in range(2, int(rt) + 1) if n % i == 0)
  s += -rt if rt.is_integer() else 1
  return s > n

for n in range(lim):
  if is_abundant(n):
    abts.add(n)
  if all(n - a not in abts for a in abts):
    ans += n

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr