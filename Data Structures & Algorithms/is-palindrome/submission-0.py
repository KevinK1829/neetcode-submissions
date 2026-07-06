class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        #iterate through each letter
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

        