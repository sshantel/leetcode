"""

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

"""


def isUgly(self, num: int) -> bool:
    if num == 0:
        return False
    while num % 2 == 0:
        num = num / 2
        print((num))
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5
    print(num)
    if num == 1:
        return True
    return False

