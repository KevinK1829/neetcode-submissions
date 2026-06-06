class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compare lengths first as a quick check
        if len(s) < len(t) : 
            return False
        #HashMap stores values in key-value pairs
        #create a HashMap to track each character as the key
        #then iterate through the string and if not present
        #set value equal to 0 else if seed at +=1 to inc value for each key
        sCount, tCount = {}, {}

        for c in s:
            if c not in sCount:
                sCount[c] = 0
            sCount[c] += 1

        for c in t:
            if c not in tCount:
                tCount[c] = 0
            tCount[c] += 1
        
        #then compare hashmaps 
        return tCount == sCount



        