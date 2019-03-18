# Note that the 6th digit must be 5; it cannot be 0 because then the 7th
# and 8th digits would need to equal each other

divs = [13, 11, 7, 5, 3, 2, 1]
us, vs = [], []

for i in range(17, 1000, 17):
  u = str(i).zfill(3)
  if "5" not in u and len(set(u)) == 3:
    us.append(u)

for d in divs:
  digits = "5" if d == 11 else "012346789"
  for u in us:
    for i in (set(digits) - set(u)):
      v = i + u
      if int(v[: 3]) % d == 0:
        vs.append(v)
  us = list(vs)
  vs.clear()

ans = sum(int(u) for u in us if u[0] != "0")

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr