class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDiffMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevDiffMap:
                return [prevDiffMap[diff], i]
            prevDiffMap[n] = i
