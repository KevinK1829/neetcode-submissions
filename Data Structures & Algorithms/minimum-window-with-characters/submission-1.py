class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #deal with test case where t is empty
        if t == "":
            return ""
        #Hash Map keeping track of total word, and window
        countT, window = {}, {}
        #populate the count of the HashMap Total string 
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        #track how much we have, and track how much we need
        have, need = 0, len(countT)
        #Since we are finding the minimum start with smallest range and length
        res, resLen = [-1, -1], float("infinity")
        l = 0
        #looping through the substring 
        for r in range(len(s)):
            #if letter in big string matches right most letter of substring
            c = s[r]
            #expand window length and add letter count to window
            window[c] = 1 + window.get(c,0)
            #
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -=  1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""