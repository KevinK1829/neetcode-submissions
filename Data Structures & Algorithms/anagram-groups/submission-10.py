class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a result list where anagram strings will be returned
        res = defaultdict(list)
        #iterate through each word
        for s in strs:
            #create a count array for each letter a...z for each word
            #anagrams words each have the same amount of letters
            count = [0] * 26
            #for each letter in each word
            for c in s:
                #increment count for each letter using ASCII
                count[ord(c) - ord("a")] += 1
                #for each word with same letter count add to result list
            res[tuple(count)].append(s)
        return list(res.values())

        


                

                


        