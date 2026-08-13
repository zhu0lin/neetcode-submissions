from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Input: Two strings s and t.
        Output: The shortest substring of s such that every character in t 
        occurs in the substring, including all of the duplicate characters
        that might appear in t

        Approach:
        This is a dynamically sized sliding window problem. This is because
        there could be letters within the substring that don't belong in t
        but we are looking for the shortest substring where all chars of t exist.

        Do we need a dictionary for this problem? We need to know the
        frequencies of each of the characters in t to be able to find
        a valid substring of s.

        Things to track:
        Starting index of substring, ending index of substring
        Frequency of characters in substring

        If we iterate over a letter that does not exist in t, we can just skip
        over it (iterate left ptr).

        MAYBE THIS SHOULD BE THE WHILE LOOP
        But at any point if we see one of the letters from t, we don't want to
        move left ptr (b/c this could the starting point of a valid substring).
        We will then expand the sliding window from this point on. 
        We'll exit out of this while loop when our substring contains
        all chars of t. We will then append this substring to an array
        and we will later return the substring with the smallest length.

        AND THEN WE CAN MOVE LEFT AFTER WE EXIT THE WHILE LOOP
        """
        # Edge case: len(s) < len(t), there can not be a valid substring of s
        if len(s) < len(t):
            return ""

        freq_t = Counter(t)
        freq_s = {}
        # for i in range(right + 1):
        #     freq_s[s[i]] = freq_s[s[i]].get(s[i], 0) + 1

        left = 0
        required = len(freq_t)
        formed = 0
        smallest_len = float('inf')
        best_window = (0, 0)

        
        for right in range(len(s)):

            char = s[right]
            freq_s[char] = freq_s.get(char, 0) + 1

            if char in freq_t and freq_s[char] == freq_t[char]:
                formed += 1

            while formed == required: # Shrink window
                if right - left + 1 < smallest_len:
                    smallest_len = right - left + 1
                    best_window = (left, right)

                left_char = s[left]
                freq_s[left_char] -= 1
                if left_char in freq_t and freq_s[left_char] < freq_t[left_char]:
                    formed -= 1
                
                left += 1

        if smallest_len == float("inf"):
            return ""

        l, r = best_window
        return s[l:r+1]

        
        
        

            

            

            
            
        



        

        
        