class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        dic = defaultdict(list)
        # we want dic to look like
        # {['a':1, 'c':1, 't':1]: ["act", "cat"], ...}

        for str in strs:
            letter_freq = [0] * 26
            for letter in str:
                letter_freq[ord(letter) - ord('a')] += 1
            dic[tuple(letter_freq)].append(str)

        return list(dic.values())