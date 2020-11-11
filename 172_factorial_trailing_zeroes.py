"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

"""


def trailingZeroes(n):

# Calculate n!
    n_factorial = 1
    for i in range(2, n + 1):
        n_factorial *= i

    # Count how many 0's are on the end.
    zero_count = 0
    while n_factorial % 10 == 0:
        zero_count += 1
        print(n_factorial)
        n_factorial //= 10
        print(n_factorial)

    return zero_count