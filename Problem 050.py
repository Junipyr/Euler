import sympy

def consec_p_sum(lim, p_sums=[0], d=0):
  p_list = list(sympy.sieve.primerange(1, lim / 100)) # /100 to save time
  while p_sums[-1] < lim:
    p_sums.append(p_sums[-1] + p_list[d])
    d += 1
  
  d -= 0 if d % 2 else 1 # We only check odd p_sums
  for i in range(d, 0, -2):
    for j in range(d - i):
      ans = p_sums[i + j] - p_sums[j]
      if ans < lim and sympy.isprime(ans):
        return ans

print(consec_p_sum(1000000))


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr