# We iterate hexagonal numbers and check whether they are pentagonal.
# By definition, every hexagonal number is a triangle number.

import math


n_h = 144
n_p = 0.5

while not n_p.is_integer():
  h = n_h*(2*n_h - 1)
  n_p = (1 + math.sqrt(1 + 24*h))/6
  n_h += 1

print(h)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr