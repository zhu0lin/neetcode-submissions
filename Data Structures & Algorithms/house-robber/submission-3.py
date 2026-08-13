class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        """
        cache = [-1, -1, -1, -1]
        cache[0] = 1 + dfs(2) 
            dfs(2) -> cache[2] = 3 + dfs(4)
            dfs(4) -> reach base case, return 0 

        cache[2] = 3
        cache[0] = 4
        """

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            print(cache)
            return cache[i]

        return dfs(0)