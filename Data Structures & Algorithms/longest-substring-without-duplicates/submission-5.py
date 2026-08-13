class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Understand:
        Input: A string s composed of characters.
        Output: An integer representing the longest substring (contiguous) without
        duplicate characters.

        Plan:
        Sliding window approach:

        """
        left = 0
        dic = {}
        res = 0

        for i in range(len(s)):
            if s[i] in dic:
                left = max(dic[s[i]]+1, left)
            dic[s[i]] = i
            res = max(res, (i-left)+1)

        return res
