import math


p_max = 1000
c_sq_set = set(c * c for c in range(p_max))
ps = [0] * p_max

for a in range(1, p_max // 2):
  for b in range(a, p_max // 2):
    c_sq = a*a + b*b
    if c_sq in c_sq_set:
      p = int(a + b + math.sqrt(c_sq))
      if p < p_max:
        ps[p] += 1
        
ans = ps.index(max(ps))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr