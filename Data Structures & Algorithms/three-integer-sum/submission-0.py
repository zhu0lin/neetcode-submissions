class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        U: 
        input: array of nums
        output: list of lists (that are the triplets) that sum to 0
        P:
        res = []
        sort the input array
        iterate over each num in nums:
        put two pointers. initially: one at the right of current num,
        other one at len(nums)-1
        if nums[curr] + nums[left] + nums[end] == 0:
            append this triplet to res
        elif nums[curr] + nums[left] + nums[end] < 0:
            move left ptr forward
        else (nums[curr] + nums[left] + nums[end] > 0):
            move end ptr left
        do all of this until nums[curr] + nums[left] + nums[end] == 0
        or left < right
        [-4, -1, -1, 0, 1, 2]
                        ^  ^
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i+1
            end = len(nums)-1
            while(left < end):
                if nums[i] + nums[left] + nums[end] == 0:
                    if [nums[i], nums[left], nums[end]] not in res:
                        res.append([nums[i], nums[left], nums[end]])
                    left += 1
                    end -= 1
                elif nums[i] + nums[left] + nums[end] < 0:
                    left += 1
                else:
                    end -= 1
            
        return res
