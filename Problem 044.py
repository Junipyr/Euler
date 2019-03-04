def pent_d():
  n = 1
  pents = set()

  while True:
    p_n = n*(3*n - 1)//2
    for p in pents:
      if p_n - p in pents and 2*p - p_n in pents:
        return 2*p - p_n
    pents.add(p_n)
    n += 1

print(pent_d())


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr