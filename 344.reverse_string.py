#! -*- coding: utf-8 -*-

"""
Write a function that takes a string as input and returns the string reversed.
"""

__author__ = 'yelongyu1024@gmail.com'


class Solution(object):
    def __init__(self, s):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

    def reverse_string_v2(self):
        return ''.join(list(reversed(self.s)))

    def reverse_string_v3(self):
        string_list = list(self.s)
        string_list.reverse()
        return ''.join(string_list)


def main():
    solution = Solution('hello')
    print solution.reverse_string()
    print solution.reverse_string_v2()
    print solution.reverse_string_v3()


if __name__ == '__main__':
    main()
