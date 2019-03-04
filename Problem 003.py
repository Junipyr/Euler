import math

n = ans = 600851475143

for x in range(2, int(math.sqrt(n)) + 1):
    if x != ans and ans % x == 0:
        ans = ans // x

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr