def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

n = 1000

ans = max(x * y
          for x in range(n)
          for y in range(n)
          if is_palindrome(str(x * y)))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr