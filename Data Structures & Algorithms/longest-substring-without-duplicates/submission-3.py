class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = float('-inf')
        left, right = 0, 1
        if len(s) == 1:
            return 1


        while right < len(s):
            arr = s[left:right+1]
            arr_set = set(arr)
            if len(arr_set) == (right-left)+1:
                if (right-left)+1 > res:
                    res = (right-left) + 1
                right += 1
            else:
                left += 1

        if res < 0:
            return 0
        else:
            return res

        return res


"""
s = "zxyzxyz"
      ^ ^
"""
