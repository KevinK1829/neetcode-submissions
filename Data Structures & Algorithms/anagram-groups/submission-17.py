class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strat return a list
        #go through each word
        #keep count of each letter for each word
        #then group them together based on if they have same counts
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


        