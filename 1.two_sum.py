# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum(self):
        nums = self.nums[:]
        if len(nums) < 2:
            return
        index_map = {}
        for index, num in enumerate(nums):
            delta = self.target - num
            if index_map.get(delta) is not None:
                return [index_map.get(delta), index]
            index_map[num] = index


def main():
    solution = Solution([3, 2, 4], 6)
    print solution.two_sum()


if __name__ == '__main__':
    main()
