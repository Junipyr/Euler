import math

n = 600851475143

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        ans = ans // i
        break

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr