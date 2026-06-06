class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need to track values and index
        #use target to know what value is needed so subtract
        #target value - index[i] = difference
            #if difference shows up in the loop thats the value we first need
            indexMap = {}
            for index, number in enumerate(nums):
                difference = target - number
                if difference in indexMap:
                    return [indexMap[difference], index]
                indexMap[number] = index
            
            
        