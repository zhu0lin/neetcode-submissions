class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)

        for s in strs:
            freq_list = [0] * 26
            for char in s:
                freq_list[ord(char) - ord('a')] += 1
            dic[tuple(freq_list)].append(s)

        return list(dic.values())