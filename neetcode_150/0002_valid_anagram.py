# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = list(s)
        second = list(t)
        first.sort()
        second.sort()
        return ''.join(first) == ''.join(second)

# Approach - Dict
