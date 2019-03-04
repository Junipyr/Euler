prev = curr = 1
i = 2

while len(str(curr)) < 1000:
  prev, curr = curr, curr + prev
  i += 1

print(i)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr