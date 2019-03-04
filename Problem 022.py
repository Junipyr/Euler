names_file = ".../p022_names.txt"
names = sorted([n.strip('"') for n in open(names_file).read().split(",")])
ans = 0

for i, n in enumerate(names):
    ans += (i + 1) * sum(ord(c) - ord("A") + 1 for c in n)

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr