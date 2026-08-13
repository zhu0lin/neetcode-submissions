class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)

        def backtrack(i, curr, picked):

            if picked[i]:
                return 

            picked[i] = True
            curr.append(nums[i])
            if len(curr) == len(nums):
                res.append(curr.copy())
                picked[i] = False
                curr.pop()
                return 

        
            # if i >= len(nums) or len(curr) >= len(nums):
            #     return

            # picked[i] = True
            # curr.append(nums[i])
            for j in range(len(nums)):
                backtrack(j, curr, picked)
            picked[i] = False
            curr.pop()
            
            
            
        for i in range(len(nums)):
            backtrack(i, [], picked)
        return res
        

        