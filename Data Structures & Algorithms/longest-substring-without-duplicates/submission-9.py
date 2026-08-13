class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        map = {}

        for i in range(len(s)):
            
            # moving left ptr
            if s[i] in map:
                left = max(left, map[s[i]] + 1)

            map[s[i]] = i
            longest = max(longest, (i - left) + 1)

        return longest
            