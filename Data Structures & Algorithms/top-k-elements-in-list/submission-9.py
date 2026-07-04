class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #Step 1
    #create a frequency array it can only be the size of list of int
    #want an array for each frequency
    #add plus one for the 0th frequency
        freq = [[] for i in range(len(nums) + 1)]
    #Step 2
    #create a count Map that stores the count of how many numbers aree
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
    #Then add number and count to the frequency array
        for n,cnt in count.items():
            freq[cnt].append(n)

    #create a result array and iterate through the frequency array
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    #starting with the most frequent (right side) and
    #append values of freq[count] to result until length of array = k
        