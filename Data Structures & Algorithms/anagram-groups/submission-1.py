class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        s
        """
        dic = defaultdict(list)
        for str in strs:
            freq_arr = [0] * 26
            for char in str:
                freq_arr[ord(char) - ord("a")] += 1

            freq_tuple = tuple(freq_arr)
            dic[freq_tuple].append(str)

        return list(dic.values())