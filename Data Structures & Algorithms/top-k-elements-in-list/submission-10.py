class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # {1:1, 2:2, 3:3}
        # bucket sort
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in freq:
            bucket[freq[num]].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
