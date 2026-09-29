class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # search forindices that antter the most

        diffMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[n] = i
        