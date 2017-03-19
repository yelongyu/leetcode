# -*- coding: utf-8 -*-

"""
Given a positive integer, output its complement number. The complement strategy
is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed
integer.
You could assume no leading zero bit in the integer’s binary representation.
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, num):
        self.num = num

    def find_complement_one(self):
        num = bin(self.num)[2:]
        full_bits = int('1' * len(num), base=2)
        return full_bits ^ self.num

    def find_complement_two(self):
        i = 1
        while i < self.num:
            i = i << 1
        return (i - 1) ^ self.num


def main():
    solution = Solution(150)
    print solution.find_complement_one()
    print solution.find_complement_two()


if __name__ == '__main__':
    main()
