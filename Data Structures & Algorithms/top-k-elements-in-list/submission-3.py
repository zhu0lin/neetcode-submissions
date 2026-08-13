class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U:
        Input: array of integers called nums
        Output: array of k integers that are the most frequent
        elements in the array nums
        
        P: Dictionary approach
        First pass: Populate the dictionary with the frequency of each integer
        in the array nums
        
        Initialize empty res array
        While loop: STOP WHEN LENGTH OF RES == K
        max_occurences = max(dic.values())
        Find key that matches max_occurences?
        Add that key to res array
        Remove that key from dictionary:
        Repeat: max_occurences = max(dic.values())

        """
        freq_dictionary = Counter(nums)
        
        res = []

        while(len(res) != k):
            max_occurences = max(freq_dictionary.values())
            for freq in freq_dictionary:
                if freq_dictionary[freq] == max_occurences:
                    res.append(freq)
                    del freq_dictionary[freq]
                    break

        return res

        

