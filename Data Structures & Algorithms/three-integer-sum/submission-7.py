class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            end = len(nums) - 1
            while j < end:
                if nums[i] + nums[j] + nums[end] == 0:
                    res.append([nums[i], nums[j], nums[end]])

                    j += 1
                    end -= 1

                    while j < end and nums[j] == nums[j - 1]:
                        j += 1

                    while j < end and nums[end] == nums[end + 1]:
                        end -= 1
                
                elif nums[i] + nums[j] + nums[end] < 0:
                    j += 1

                else:
                    end -= 1

            
        return res