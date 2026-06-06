class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step 1 make result HashMap but it has to be defaultdict(list) so we can append 
        #key values starting with an empty list
        #Step 2: loop through words and create count array of size 26
        #Step 3: loop through each letter in the word and add counts using ASCII

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a..z
            for c in s:
                #ASCII Language
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())


        
        
        