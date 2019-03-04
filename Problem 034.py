# First, 9! * 7 = 2540160 is an upper bound for our search.
# This can be further improved to 1500000.
# See https://en.wikipedia.org/wiki/Factorion for details.

import math


ans = 0
facts = [math.factorial(i) for i in range(10)]

for n in range(10, 1500000, 10):
  m = n
  fact_sum = 0
  while m > 0:
    fact_sum += facts[m % 10]
    m //= 10
  for i in range(10):
    if fact_sum + facts[i] - 1 == n + i:
      ans += n + i

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr