class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sMap, tMap = {}, {}

        for c in range(len(s)):
            sMap[s[c]] = 1 + sMap.get(s[c],0)
        for c in range(len(t)):
            tMap[t[c]] = 1 + tMap.get(t[c],0)
        return sMap == tMap