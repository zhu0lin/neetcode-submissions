import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      """
      U:
      Input: a string with only uppercase characters and an integer k
      Output: res, An integer of the longest contiguous substring
      
      P:
      Sliding window with two pointers (for lhs and rhs of window)
      start left at 0, right at 0
      initialize res, An integer of the longest contiguous substring
      initialize number of replacements to 0

      update freq map
      distinct character
      if it does, move right forward and update res
      if it doesn't, update number of replacements
      """  
      if len(s) == 1:
        return 1
      left = 0
      right = 0
      max_freq = 0
      best_len = 0
      freq_map = collections.Counter()
      
      while right < len(s):
        freq_map[s[right]] += 1
        max_freq = max(max_freq, freq_map[s[right]])


        while (right-left+1) - max_freq > k:
            freq_map[s[left]] -= 1
            left += 1
        best_len = max(best_len, right - left + 1)
        right += 1


      return best_len
      """
      "AAABABB"
       ^   ^
      """
