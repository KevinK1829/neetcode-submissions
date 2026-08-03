class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #output an array of indices
        res = []
        #difference = target - current
        #track difference in HashMap so if run into it pull its key in
        #value : index
        diffMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[n] = i


