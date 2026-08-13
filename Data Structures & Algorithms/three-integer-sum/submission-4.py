class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Input: An array of integers nums
        Output: An array of all triplets with indices i, j, k where 
        nums[i] + nums[j] + nums[k] = 0. 
        Return the index values. No duplicate triplets and 
        we can return the triplets in any order.

        Two pointer approach with loop

        """
        nums.sort()
        res = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1

            while left < right:
                
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                    

                    
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                
                else:
                    right -= 1

        return res
                    
                    
