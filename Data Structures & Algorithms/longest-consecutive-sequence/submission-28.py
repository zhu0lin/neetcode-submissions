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

        # 2, 3, 4, 5, 10, 20
        # 0, 1, 2, 3, 4, 5, 6
        if not nums: 
            return 0
        freq_map = Counter(nums)

        possible_res = []
        curr_res = 0
        nums = list(sorted(set(nums)))
        for i in range(len(nums)):
            if nums[i]-1 not in freq_map:
                possible_res.append(curr_res)
                curr_res = 1
            elif nums[i]-1 in freq_map and nums[i] != nums[i-1]:
                curr_res += 1



        possible_res.append(curr_res)

        return max(possible_res) 
            
