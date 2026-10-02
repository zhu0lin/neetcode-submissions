class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)

        res = 0
        for num in freq:
            if num - 1 not in freq:
                count = 1
                while num + count in freq:
                    count += 1
                res = max(res, count)

        return res
                


            