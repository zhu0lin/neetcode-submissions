class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        U:
        Input: an integer array nums (can be pos or neg numbers)
        Output: an integer array output where each number is the 
        product of all other numbers in the nums array
        
        P:
        Initialize a pre arr that contains of product of integers
        from left to right
        Initialize a suff arr that contains of product of integers 
        from right to left

        After this, in example 1, pre and suff arrs will look like:
        pre = [1, 1, 2, 8]
        suff = [48,24,6,1]
        Initialize res array, that multiplies left product with right product
        res = [48, 24, 12, 8]
        """
        pre = [0] * len(nums)
        suff = [0] * len(nums)
        res = [0] * len(nums)

        prod = 1
        for i in range(len(nums)):
            pre[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            suff[i] = prod
            prod *= nums[i]

        for i in range(len(res)):
            res[i] = pre[i] * suff[i]

        return res
            

