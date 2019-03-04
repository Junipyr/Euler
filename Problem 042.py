words_file = ".../words.txt"
words = [n.strip('"') for n in open(words_file).read().split(",")]
triangles = set(n*(n + 1)/2 for n in range(1, 30))
ans = 0

for w in words:
  w_value = sum(ord(l) - ord("A") + 1 for l in w)
  if w_value in triangles:
    ans += 1

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr