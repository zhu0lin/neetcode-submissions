class Solution:
    from collections import Counter
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U: 
        input: an array of nums 
        output: an integer of the longest consecutive sequence
        
        P: 
        Initialize empty dict
        Iterate over nums and populate the dict with the frequency of each num
        Sort the input array
        Have a res of 0
        Iterate over the sorted input array,
        Check frequency of current num, if it exists, increase res
        """

        nums_set = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                curr_longest = 0
                while(nums[i]+curr_longest in nums_set):
                    curr_longest += 1
                res = max(res, curr_longest)
        
        return res
            
