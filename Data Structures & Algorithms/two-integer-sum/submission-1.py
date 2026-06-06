class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Step1 create Prev Map to track prior difference values; value:index
        #Step2 iterate through the array using enumeration to track value, index
        #Step3 while itearting find the difference between target and value
        #Step4 if difference is found pull difference, and current index
        #Step5 if not found add the current index you are in to the HashMap

        prevMap = {}

        for i,n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i