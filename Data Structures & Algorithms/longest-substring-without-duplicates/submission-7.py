class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0

        curr_set = set()

        for i in range(len(s)):

            # if s[right] not in curr_set:
            #     curr_set.add(s[right])
            #     longest = max(longest, (right - left)+1)
            # else:
            while s[i] in curr_set:
                curr_set.remove(s[left])
                left += 1

            curr_set.add(s[i])
            longest = max(longest, (i - left) + 1)

        return longest
            