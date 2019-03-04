fractional = "".join([str(i) for i in range(1, 200000)])
ans = 1

for j in range(7):
  ans *= int(fractional[10**j - 1])

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr