# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for char in s:
            if stack == []:
                stack.append(char)
            else:
                if char in mapping:
                    stack.append(char)
                elif stack[-1] in mapping and mapping[stack[-1]] == char:
                    stack.pop()  
                else:
                    return False

        if stack == []:
            return True
        else:
            return False
        
