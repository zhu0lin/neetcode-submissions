class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Understand
        Input: An array of integers nums
        Output: An array of arrays of all possible subsets. 

        Plan
        Base case: len(nums) == 0, add [] to output array

        Recursive case: 
        """
        res = []
        subset = []

        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # don't include nums[i]
            subset.pop()
            backtrack(i + 1)


        backtrack(0)
        return res
