ans = 0
curr = prev = 1

while curr <= 4000000:
    prev, curr = curr, prev + curr
    if prev % 2 == 0:
        ans += prev

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr