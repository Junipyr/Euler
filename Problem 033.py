import math


m = n = 1
for i in range(10, 100):
  for j in range(i + 1, 100):
    u = [int(d) for d in str(i)]
    v = [int(d) for d in str(j)]
    if v[1] != 0 and u[1] == v[0] and i / j == u[0] / v[1]:
      m *= i
      n *= j

ans = n // math.gcd(m, n)

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr