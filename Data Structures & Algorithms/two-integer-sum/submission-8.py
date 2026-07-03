class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #track index and values, using hashmao
        #going to iterate through num tracking index and num
        #know diff = n - target
        #if diff found in prior return those 2 indices
        prevMap = {} #value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:    
                return [prevMap[diff],i]
            prevMap[n] = i

        