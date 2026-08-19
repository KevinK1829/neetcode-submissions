class Solution:
    def isValid(self, s: str) -> bool:
        #LIFO most recent unsolved thing needs to be dealt with first
        stack = []

        mapBracket = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in mapBracket:
                if stack and mapBracket[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False







        
        