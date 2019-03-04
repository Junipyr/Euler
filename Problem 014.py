def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

i_max = 999999
lengths = [0] * i_max
lengths[0] = 1

for i in range(1, i_max):
    n = i + 1
    n_list = []
    while n >= i_max or lengths[n - 1] == 0:
        n_list.append(n)
        n = collatz(n)
    for j in range(len(n_list)):
        if n_list[j] <= i_max:
            lengths[n_list[j] - 1] = len(n_list) - j + lengths[n - 1]

print(lengths.index(max(lengths)) + 1)  # numpy.argmax() would be even faster


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr