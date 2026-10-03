class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = {}
        l = 0

        for r in range(len(s)):
            
            dic[s[r]] = dic.get(s[r], 0) + 1
            most_freq  = max(dic.values())
            replacements_needed = (r - l + 1) - most_freq

            if replacements_needed > k:
                dic[s[l]] -= 1
                l += 1
                

            res = max(res, r - l + 1)
            

        return res

        