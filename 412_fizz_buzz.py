"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
""" 

import unittest

class TestStringMethods(unittest.TestCase):

    def test_sol(self):
        fb = Solution()
        self.assertEqual(fb.fizzBuzz(3), ["1","2","Fizz"])
        self.assertEqual(fb.fizzBuzz(5), ["1","2","Fizz","4","Buzz"])
        self.assertEqual(fb.fizzBuzz(15),["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
        
class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer


if __name__ == '__main__':
    unittest.main()