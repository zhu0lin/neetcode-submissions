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
        (act, cat): {a: 1, c:1, t:1}
        """
        my_dict = defaultdict(list)
        for word in strs:
            alphabet = [0] * 26
            for char in word:
                alphabet[ord(char) - ord('a')] += 1
            if tuple(alphabet) in my_dict:
                my_dict[tuple(alphabet)].append(word)
            else:
                my_dict[tuple(alphabet)] = [word]

        res = list(my_dict.values())
        return res


        