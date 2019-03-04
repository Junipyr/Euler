# We could just use numbers of letters per word and omit spaces and
# hyphens, but it's nicer to convert the numbers fully.


def num_to_words(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen",
             "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]

    if n < 1000000:
        num_list = []
        if n >= 1000:
            num_list.append(num_to_words(n // 1000) + " thousand ")
            if ((n // 1000) < 100 and (n % 1000) != 0):
                num_list.append(" and ")
        if n % 1000 >= 100:
            num_list.append(str(units[(n % 1000) // 100]))
            num_list.append(" hundred" if n % 100 == 0 else " hundred and ")
        if n % 100 >= 20:
            num_list.append(str(tens[(n % 100) // 10]))
            if (n % 10 != 0):
                num_list.append("-" + str(units[n % 10]))
        if n % 100 < 20:
            num_list.append(str(units[n % 100]))
        return("".join(num_list).strip())
    else:
        raise ValueError("Only numbers below 1,000,000 are supported.")

i_max = 1000
ans = 0

for i in range(1, i_max + 1):
    ans += len(num_to_words(i).replace(" ", "").replace("-", ""))

print(ans)


# Copyright Junipyr. All rights reserved.
# https://github.com/Junipyr