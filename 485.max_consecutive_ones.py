# -*- coding: utf-8 -*-

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def find_max_consecutive_ones(self):
        nums = ''.join(map(str, self.nums))
        nums = nums.split('0')
        return len(max(nums))


def main():
    solution = Solution([1, 1, 0, 1, 1, 1])
    print solution.find_max_consecutive_ones()


if __name__ == '__main__':
    main()
