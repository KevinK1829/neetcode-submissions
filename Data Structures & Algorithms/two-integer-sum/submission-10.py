class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevDiffMap = {}
        res = []

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevDiffMap:
                res = [prevDiffMap[diff], i]
            prevDiffMap[n] = i
        return res


