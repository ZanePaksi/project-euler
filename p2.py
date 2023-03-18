# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

fib_nums = [0, 1]


def main(index):
    next_num = fib_nums[index - 1] + fib_nums[index]
    if next_num > 4000000:
        even_fibs = [num for num in fib_nums if num % 2 == 0]
        return sum(even_fibs)

    fib_nums.append(next_num)
    return main(index + 1)


print(main(1))