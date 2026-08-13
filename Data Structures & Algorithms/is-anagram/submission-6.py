class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alpha = [0] * 26
        t_alpha = [0] * 26

        for char in s:
            s_alpha[ord('z') - ord(char)] += 1

        for char in t:
            t_alpha[ord('z') - ord(char)] += 1

        if s_alpha == t_alpha:
            return True
        else:
            return False