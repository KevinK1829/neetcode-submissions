class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #list of numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]
        #count frequency of numbers
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #add to buckets, n = number,  c = count
        for n, c in count.items():
            freq[c].append(n)
        #create result variable
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            