class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #cant have empty keys
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            #tuple since count is an array
            res[tuple(count)].append(s)
        return list(res.values())
                

                


        