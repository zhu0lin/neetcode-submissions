class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_alpha = [0] * 26
        # t_alpha = [0] * 26

        # for char in s:
        #     s_alpha[ord('z') - ord(char)] += 1

        # for char in t:
        #     t_alpha[ord('z') - ord(char)] += 1

        # if s_alpha == t_alpha:
        #     return True
        # else:
        #     return False

        """
        Instead of doing the above, where we have two arrays
        of s_alpha and t_alpha, representing the number of occurences
        for each letter in s and t respectively

        We can have one array count. Iterating over both s and t at the same time,
        we add occurences of s into count and remove occurences of t from count.
        This way, if the occurences of a letter in s is the same as the occurences
        in t, the occurence in the count array of that letter should be 0
        """
        count = [0] * 26
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[ord('z') - ord(s[i])] += 1
            count[ord('z') - ord(t[i])] -= 1

        for occurence in count:
            if occurence != 0:
                return False

        return True