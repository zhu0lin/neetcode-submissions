class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]
        # bucket = [[], [], [], []]
        
        for element in freq:
            frequency = freq[element]
            bucket[frequency].append(element)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res