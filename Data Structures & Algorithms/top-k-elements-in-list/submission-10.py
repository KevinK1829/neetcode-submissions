class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Step 1: Create frequency array and count HashMap
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #Step 2: Add counts to hash map
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #Step 3: Add number and count to frequency array
        for n,cnt in count.items():
            freq[cnt].append(n)
        #Step 4: Create result array
        res = []
        #Step 5: go through frequency array and add numbers to result
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
        #Step 6: Stop once it kth frequent element and return
                if len(res) == k:
                    return res
       
   