#! -*- coding: utf-8 -*-

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.
"""


__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, n):
        self.n = n

    def fizz_buzz(self):
        result = []
        for i in xrange(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

    # fabulous!!!
    def fizz_buzz_v2(self):
        return ['Fizz'*(not i % 3) + 'Buzz'*(not i % 5) or str(i)
                for i in range(1, self.n+1)]


def main():
    solution = Solution(15)
    print solution.fizz_buzz()
    print solution.fizz_buzz_v2()


if __name__ == '__main__':
    main()
