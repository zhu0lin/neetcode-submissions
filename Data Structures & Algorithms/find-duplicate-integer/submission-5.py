class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Understand
        Input: An array of integers nums. The array is unsorted. The integers in nums
        are in the range of 1 to len(nums)-1 inclusive
        Output: An integer that appears more than once in the array nums

        Possible cases:
        0   1  2  3  4
        [1, 1, 2, 3, 4]

        Plan:
        O(n) time and O(1) space. Meaning we're probably doing 2 ptr?
        Maybe just leave one ptr at nums[-1]? That way when we iterate
        over nums, we can just constantly compare our current value 
        """
        
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1