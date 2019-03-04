s = set()

for i in range(1, 100):
  for j in range(100, 10000 // i):
    if set(str(i) + str(j) + str(i * j)) == set("123456789"):
      s.add(i * j)

print(sum(s))


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr