class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        longest = 0
        
        
        for num in dic:
            
            if num - 1 not in dic:
                length = 1
                while num + length in dic:
                    length += 1
                longest = max(longest, length)


        return longest
