class Solution:

    def encode(self, strs: List[str]) -> str:
        #create empty string
        res = ""
        #iterate through each word and then append length of word + # as code
        for s in strs:
            res += str(len(s)) + "#" + s
        #return result
        return res

    def decode(self, s: str) -> List[str]:
        #create an array and track index
        res, i = [], 0
        #check for index to be less than string
        while i < len(s):
            #create a tracker variable
            j = i
            #increment until you hit #
            while s[j] != "#":
                j += 1
            #get the length of start 
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
