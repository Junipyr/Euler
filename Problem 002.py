ans = 0
x = y = 1

while x <= 4000000:
    x, y = y, x + y
    if x % 2 == 0:
        ans += x

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr