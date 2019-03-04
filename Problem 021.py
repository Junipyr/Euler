n_max = 10000
s = [0] * n_max
ans = 0

for n in range(1, n_max):
  s[2*n::n] = [x + n for x in s[2*n::n]]
  if s[n] < n and n == s[s[n]]:
    ans += n + s[n]

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr