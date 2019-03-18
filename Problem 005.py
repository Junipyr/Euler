import math

def lcm(a, b):
    return int(a * b / math.gcd(a, b))

ans = 1
for d in range(10, 20):
    ans = lcm(ans, d + 1)

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr