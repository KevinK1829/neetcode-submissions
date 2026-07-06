class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #get set of nums
        numSet = set(nums)
        #initialize longest sequence
        longest = 0

        for n in numSet:
            length = 1
            if (n - 1) not in numSet:
                curr = n
                while (curr + 1) in numSet:
                    length += 1
                    curr += 1
            longest = max(length, longest)
        
        return longest
