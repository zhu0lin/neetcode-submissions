class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: A string with only uppercase characters and an integer k
        Output: An integer representing the length of the longest
        substring with only one distinct character

        Approach: Sliding window
        Expand window when num_replacements <= k
        Shrink when num_replacements > k
        """
        left = 0
        longest = 0
        greatest_freq = 0
        dic = {}

        for i in range(len(s)):

            dic[s[i]] = dic.get(s[i], 0) + 1
            greatest_freq = max(greatest_freq, dic[s[i]])

            # Shrink 
            while (i - left + 1) - greatest_freq > k:
                dic[s[left]] -= 1
                left += 1

            longest = max(longest, i - left + 1)

        return longest
            


