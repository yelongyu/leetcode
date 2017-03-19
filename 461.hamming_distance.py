# -*- coding: utf-8 -*-

"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
"""

__author__ = 'yelongyu1024@gmail.com'

import re


class Solution(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hamming_distance(self):
        print 'x:   {0:032b}'.format(self.x)
        print 'y:   {0:032b}'.format(self.y)
        print 'x&y: {0:032b}'.format(self.x & self.y)
        print 'x|y: {0:032b}'.format(self.x | self.y)
        print 'x^y: {0:032b}'.format(self.x ^ self.y)
        return len(re.findall('1', str(bin(self.x ^ self.y))))


def main():
    solution = Solution(100, 111)
    print solution.hamming_distance()


if __name__ == '__main__':
    main()
