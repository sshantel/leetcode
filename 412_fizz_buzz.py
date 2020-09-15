"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def div_by_3(num):
            return num % 3 == 0 
        def div_by_5(num):
            return num % 5 == 0
        fizz_buzz_list = []
        i = 1
        while i < n:
            if div_by_3(i) and div_by_5(i):
                fizz_buzz_list.append("FizzBuzz")
            elif div_by_3(i):
                fizz_buzz_list.append("Fizz")
            elif div_by_5(i):
                fizz_buzz_list.append("Buzz")
            else:
                fizz_buzz_list.append(i)
            i += 1
        return fizz_buzz_list 