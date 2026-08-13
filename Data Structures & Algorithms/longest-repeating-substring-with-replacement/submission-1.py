class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = float('-inf')
        dic = {}

        while(right < len(s)):
            if s[right] not in dic:
                dic[s[right]] = 1
            else:
                dic[s[right]] += 1

            while ( ((right-left) + 1) - (max(dic.values()))  > k ):
                dic[s[left]] -= 1
                left += 1
            res = max((right-left) + 1, res)
            right += 1

            # if ((right-left)+1) - max(dic.keys()) > k:
            #     dic[left] -= 1
            #     left += 1
            # else:
            #     if (right-left) + 1 > res:
            #         res = (right-left) + 1
            #     right += 1
            

        return res
            
