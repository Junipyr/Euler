def pyth_triplet(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None

ans = pyth_triplet(1000)

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr