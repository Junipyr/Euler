import itertools


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = next(itertools.islice(itertools.permutations(digits), 999999, None))

print("".join(str(d) for d in ans))


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr