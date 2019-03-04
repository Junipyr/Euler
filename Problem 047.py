n_max = 150000
f = [0] * n_max

for n in range(2, n_max - 4):
  if f[n] == 0:
    f[n::n] = [x + 1 for x in f[n::n]]
  elif f[n:n + 4] == [4, 4, 4, 4]:
    ans = n
    break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr