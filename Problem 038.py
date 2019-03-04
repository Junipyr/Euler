# We require n = 2 or n = 5, as n = 3 or 4 can't give 9 digits

for n in range(9487, 9213, -1):
  conc = str(n) + str(2 * n)
  if set(conc) == set("123456789"):
    ans = max(conc, 918273645)
    break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr