class Solution:
    def isValid(self, s: str) -> bool:
        #LIFO most recent unsolved thing needs to be dealt with first
        stack = []
        #create HashMap
        openBracketMap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in openBracketMap:
                if stack and openBracketMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False





        
        