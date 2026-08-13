class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        U:
        Input: an array of strings
        Output: an array of arrays, with each array containing 
        strings that are anagrams of each other

        P:  
        Dictionary approach
        Initialize defaultdict of type dictionary
        Example of what the dictionary would look like when populated:
        (act, cat): []
        """
        dic = defaultdict(list)
        for str in strs:
            alphabet = [0] * 26
            for char in str:
                alphabet[ord(char)- ord('a')] += 1
            if tuple(alphabet) in dic:
                dic[tuple(alphabet)].append(str)
            else:
                dic[tuple(alphabet)] = [str]

        res = list(dic.values())
        return res


        