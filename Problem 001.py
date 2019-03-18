n = 999

ans = sum(((n//i)**2 + (n//i))*i//2 for i in [3, 5, -15])

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr