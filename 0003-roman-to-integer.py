# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.
# Edge cases IV, IX

class Solution:        

    def romanToInt(self, s: str) -> int:
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        length = len(s)
        index = 0
        while index < length:
            current_ch = s[index]
            if index != length-1:
                next_ch = s[index+1]
                value = mapping[next_ch] - mapping[current_ch]
                if value <= 0:
                    total = total + mapping[current_ch]
                    index = index + 1
                else:
                   total = total + value
                   index = index + 2 
            else :
                total = total + mapping[current_ch]
                index = index + 1
        return total


# Better solution
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
        
