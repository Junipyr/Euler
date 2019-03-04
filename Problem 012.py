import math


def divisors(n):
    l = []
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            l.append(i)
            l.append(n // i)
    l.sort()
    return(l)

i = ans = 0
while len(divisors(ans)) < 500:
    i += 1
    ans += i

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr