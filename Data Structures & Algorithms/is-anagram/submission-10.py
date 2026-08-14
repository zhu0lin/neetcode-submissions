class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic = {}
        for letter in t:
            dic[letter] = dic.get(letter, 0) + 1

        for letter in s:
            count = s.count(letter)
            if dic.get(letter, -1) == -1 or dic[letter] != count:
                return False

        return True