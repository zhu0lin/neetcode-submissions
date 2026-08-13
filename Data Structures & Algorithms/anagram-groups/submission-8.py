class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) in dic:
                dic[tuple(freq)].append(word) 
            else:
                dic[tuple(freq)] = [word]

        # dic = {[1, 0, 0, ]: ["hat"], [1, 0, 0]: ["act"], ...}

        for key in dic:
            res.append(dic[key])
        return res