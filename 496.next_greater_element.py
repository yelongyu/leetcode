#! -*- coding: utf-8 -*-

"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]

Explanation:
    For number 4 in the first array, you cannot find the next greater number
for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the
second array is 3.
    For number 2 in the first array, there is no next greater number for
it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]

Explanation:
    For number 2 in the first array, the next greater number for it
in the second array is 3.
    For number 4 in the first array, there is no next greater
number for it in the second array, so output -1.

Note:
    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.


[one more step]:

    you should figure out what is the next greater number first, or you can
not do it right.

for example:
    Input: nums1 = [2,4], nums2 = [1,2,3,4].

    init result = []

    1. the first element in list num1 is 2, so we need find 2 in list num2
first, then we found it's index in num2 is 1, next we should find a number
bigger than 2 in nums2[1:], we found 3 is bigger than 2! result = [3].

    2. the second number in list nums1 is 4, we found that the index of 4 in
list nums2 is 3, and also it's the last element in nums2, so, there is no more
number can be bigger than 4, we add -1 to the result.


    3. finally: Output: [3,-1]
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, find_nums, nums):
        self.find_nums = find_nums
        self.nums = nums

    def next_greater_element(self):
        result = []
        for num1 in self.find_nums:
            index = self.nums.index(num1)
            for num2 in self.nums[index:]:
                if num2 > num1:
                    result.append(num2)
                    break
            else:
                result.append(-1)
        return result


def main():
    solution = Solution([4, 1, 2], [1, 3, 4, 2])
    print solution.next_greater_element()


if __name__ == '__main__':
    main()
