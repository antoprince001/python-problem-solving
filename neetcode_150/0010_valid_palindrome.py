# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = True
        i = 0
        j = len(s) - 1
        while i < j:
            if not (s[i].isalpha() or s[i].isdigit())  :
                i = i + 1
            elif not (s[j].isalpha() or s[j].isdigit()) :
                j = j - 1
            elif s[i].lower() == s[j].lower():
                i = i + 1
                j = j - 1
            else:
                return False
        return True
        
