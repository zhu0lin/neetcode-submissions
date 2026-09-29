class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        freq = Counter(nums) # {1:1, 2:2, 3:3}

        bucket = [[] for _ in range(len(nums) + 1)] # [[], [], [], []]

        for num in freq: # [[1], [2], [], [3]]
            bucket[freq[num]].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        