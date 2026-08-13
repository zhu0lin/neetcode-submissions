class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        U:
        Input: An array with all values being unique. Originally
        sorted, but now rotated.
        P:
        Binary search:

        """
        l = 0
        r = len(nums)-1

        while (l < r):
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1

        return nums[l]