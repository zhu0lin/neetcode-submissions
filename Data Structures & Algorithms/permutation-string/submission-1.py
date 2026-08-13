class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        U:
        Input: two strings s1 and s2, composed of only lowercase letters
        We want to return True if s1 exists as a substring of s2
        and False otherwise

        P:
        Approach: Sliding window
        Statically sized sliding window (of len s1) on s2
        Sort current window. Check if this window exists IN s1
        If it does, return True
        """

        s1_bucket = [0] * 26
        s2_bucket = [0] * 26
    
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            s1_bucket[idx] += 1
        
        for ch in s2[:len(s1)]:
            s2_bucket[ord(ch)-ord('a')] += 1

        # check first window
        if s1_bucket == s2_bucket:
            return True
        
        for i in range(len(s1), len(s2)):
            out_ch = s2[i-len(s1)]
            in_ch = s2[i]
            s2_bucket[ord(out_ch)-ord('a')] -= 1
            s2_bucket[ord(in_ch)-ord('a')] += 1
            
            if s1_bucket == s2_bucket:
                return True
            
        return False

        

