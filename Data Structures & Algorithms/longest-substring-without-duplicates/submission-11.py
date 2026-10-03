class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dic = {}
        l = 0

        for r in range(len(s)):
            if s[r] in dic:
                l = max(dic[s[r]] + 1, l)
            dic[s[r]] = r
            res = max(res, r - l + 1)
            

        return res

