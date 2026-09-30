class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: an array nums of integers
        Output: an array of length nums where nums[i]
        represents the product of all other intgeers in nums 
        except for nums[i] itself


        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # res = [1, 1, 2, 8]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res