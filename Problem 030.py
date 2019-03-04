i_max = 354295 # We can only reach (9^5)*6 = 354294 with powers of five.

ans = sum(i for i in range(2, i_max) if i == sum(int(c) ** 5 for c in str(i)))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr