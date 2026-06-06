class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1: iterate through each word 
        #2: go through each character in each word and stores the counts
        #of that and compare if they are equal and pull index and add
        #index to the map

        res = {}
        for word in strs:
            key = "".join(sorted(word))   # anagrams → same key
            if key not in res:
                res[key] = []             # start an empty list
            res[key].append(word)         # drop this word in its bucket
        return list(res.values())
            



