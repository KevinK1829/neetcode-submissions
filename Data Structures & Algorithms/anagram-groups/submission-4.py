class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a list of results make it a default dict since it initializes into []
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #create a count for each letter
            for c in s:
                count[ord(c) - ord("a")] += 1 #increment the count for each letter you see
            res[tuple(count)].append(s) #assign word to respective count since it will
                #group anagrams since anagrams have the same amount of lettersm 
        return list(res.values()) 
