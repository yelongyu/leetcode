# -*- coding: utf-8 -*-

"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard.
"""

__author__ = 'yelongyu1024@gmail.com'


KEYBOARD = {
    'row1': ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    'row2': ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    'row3': ['z', 'x', 'c', 'v', 'b', 'n', 'm']}


class Solution(object):
    def __init__(self, words):
        self.words = words

    def find_words(self):
        results = []
        for word in self.words:
            if word[0].lower() in KEYBOARD['row1']:
                for c in word:
                    if c.lower() not in KEYBOARD['row1']:
                        break
                else:
                    results.append(word)
            elif word[0].lower() in KEYBOARD['row2']:
                for c in word:
                    if c.lower() not in KEYBOARD['row2']:
                        break
                else:
                    results.append(word)
            elif word[0].lower() in KEYBOARD['row3']:
                for c in word:
                    if c.lower() not in KEYBOARD['row3']:
                        break
                else:
                    results.append(word)
        return results

    def find_words_v2(self):
        line1 = KEYBOARD['row1']
        line2 = KEYBOARD['row2']
        line3 = KEYBOARD['row3']
        results = []
        for word in self.words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                results.append(word)
        return results


def main():
    solution = Solution(['Hello', 'Alaska', 'Dad', 'Peace'])
    print solution.find_words()
    print solution.find_words_v2()


if __name__ == '__main__':
    main()
