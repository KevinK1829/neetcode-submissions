class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first check lengths
        if len(s) != len(t):
            return False

        # hash tables needed to track frequency
        sfrequency = {}
        tfrequency = {}

        #loop thorugh strings and set frequency values for every char
        for c in s:
            #the not statement is needed to set characters not seen to 0
            if c not in sfrequency:
                sfrequency[c] = 0
            #if seen increment by 1
            sfrequency[c] += 1    
            
        for c in t:
            if c not in tfrequency:
                tfrequency[c] = 0
            tfrequency[c] += 1

        #checks logic to see if s and t strings are anagrams
        return tfrequency == sfrequency


