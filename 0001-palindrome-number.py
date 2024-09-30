# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def reverse_number(self, x: int):
        reversed_x = 0
        while x!=0:
            digit = int(x%10)
            reversed_x = reversed_x*10 +  digit
            x = int(x/10)
        return reversed_x

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == self.reverse_number(x):
            return True
        else:
            return False

# Better Approaches
# Reversing Half of the Number
