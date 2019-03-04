# This problem can be solved analytically, but we can just as well use
# a for loop. For a given shell of side n, the value at the top right
# vertex is given by the area, n^2. Moving anticlockwise, the values at
# the other vertex is always (n - 1) less than the previous vertex.

n_max = 1001

ans = 1 + sum(4*n**2 - 6*(n - 1) for n in range(3, n_max + 1, 2))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr