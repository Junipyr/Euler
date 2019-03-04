# For a square grid of side n, there are n horizontal and n vertical
# moves required.  Any individual horizontal (vertical) move is
# indistinguishable from any other, so we have 2*n choose n routes.

import sympy

n = 40
k = 20

ans = int(sympy.binomial(n, k))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr