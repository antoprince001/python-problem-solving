# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

# Floyd's cycle detection / Tortoise and hare approach
class Solution:
    def sumOfSquareOfDigits(self, n : int) -> int:
        sum_of_square = 0
        while n != 0:
            digit = n%10
            sum_of_square += digit*digit
            n = n//10
        return sum_of_square

    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        while n >= 10:
            sum_of_square_of_digits = self.sumOfSquareOfDigits(n)
            if sum_of_square_of_digits == 1 or sum_of_square_of_digits == 7:
                return True
            n = sum_of_square_of_digits
        return False


class Solution:
    def sumOfSquareOfDigits(self, n : int) -> int:
        sum_of_square = 0
        while n != 0:
            digit = n%10
            sum_of_square += digit*digit
            n = n//10
        return sum_of_square

    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        past_sums = []
        while n > 0:
            sum_of_square_of_digits = self.sumOfSquareOfDigits(n)
            if sum_of_square_of_digits == 1 or sum_of_square_of_digits == 7:
                return True
            if sum_of_square_of_digits in past_sums:
                break
            n = sum_of_square_of_digits
            past_sums.append(n)
        return False
        
      
class Solution:
    def sumOfSquareOfDigits(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquareOfDigits(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquareOfDigits(slow)
            fast = self.sumOfSquareOfDigits(self.sumOfSquareOfDigits(fast))

        return fast == 1

        
