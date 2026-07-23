class Solution:
    def isValid(self, s: str) -> bool:
        openCloseMap = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for c in s:
            if c in openCloseMap: 
                if stack and openCloseMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            