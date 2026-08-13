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
        nums.sort() # sort so we can use two pointer method effectively
        res = []

        for i in range(len(nums)-2): # we can stop at the 3rd to last value
                                    # in the array bc we're looking for triplets

            if i > 0 and nums[i] == nums[i-1]: # we can skip values that we see again
                continue

            left = i + 1 # during each iteration, we move left forward
            right = len(nums)-1

            while left < right:
                
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1 # move left and right forward to check for further valid triplets
                    right -= 1
                    while nums[left] == nums[left-1] and left < right: 
                    # skip duplicates. the left < right condition prevents out from going of bounds in an array like [0, 0, 0] 
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                    # skip duplicates. the left < right condition prevents out from going of bounds in an array like [0, 0, 0] 
                        right -= 1
                    
                elif nums[i] + nums[left] + nums[right] < 0: 
                    left += 1
                
                else:
                    right -= 1

        return res
                    
                    
