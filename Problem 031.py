amt = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*amt

for c in coins:
    for i in range(c, amt + 1):
        ways[i] += ways[i - c]

print(ways[amt])


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr