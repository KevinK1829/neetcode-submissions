class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #create a map to track previous values
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
    #iterate throgh the integers in the list
    # for each inetger track the differnec by keeping track
    #of target minus current target
    #then look back for previous difference and if its spotted
    #we can then pull the index we saw it on
    # if its not spotted add the index you are on to the map
    #also not map will be set up like value:index since we need to
    #return index so useful to keep track of index and value

       