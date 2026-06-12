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
            j = i
            #create a tracker variable
            while s[j] != "#":
                j += 1
            #increment until you hit #
         
            #get the integer length by getting number value in front of string
            length = int(s[i:j])
            #get the first non int,# charcter until the length is reached
            res.append(s[j + 1:j + 1 + length])
            #then repeat by setting index to start of next word
            i = j + 1 + length
        #return result
        return res
