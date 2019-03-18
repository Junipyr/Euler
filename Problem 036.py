ans = 1 + 3 + 5 + 7 + 9 # Trivial solutions
mid = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(1, 1000):
  if i == 100:
    mid = [""]
  s = str(i)
  if s[0] in "02468": # Even numbers can't be binary palindromes
    continue
  for j in mid:
    d = int(s + j + s[:: -1]) # Decimal palindrome
    b = str(bin(d))[2: ] # Binary
    if b == b[:: -1]:
      ans += d

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr