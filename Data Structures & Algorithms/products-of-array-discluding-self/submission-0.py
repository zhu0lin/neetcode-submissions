class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        U:
        Input: an integer array nums (can be pos or neg numbers)
        Output: an integer array output where each number is the 
        product of all other numbers in the nums array
        
        P:

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
            

