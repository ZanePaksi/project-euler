# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

import sys


def main():
    top_value = int(sys.argv[1])
    mult_3 = [num for num in range(0, top_value, 3)]
    mult_5 = [num for num in range(0, top_value, 5)]
    total_mult = list(dict.fromkeys(mult_3 + mult_5))

    print(f"Sum :: {sum(total_mult)}")


main()
