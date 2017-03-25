# -*- coding: utf-8 -*-
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def find_disappeared_numbers(self):
        set_1 = set(self.nums)
        set_2 = set(xrange(1, len(self.nums) + 1))
        return list(set_2 - set_1)


def main():
    solution = Solution([4, 3, 2, 7, 8, 2, 3, 1])
    print solution.find_disappeared_numbers()


if __name__ == '__main__':
    main()
