class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        res = 0
        for i in range(len(prefix)):
            prefix[i] = max(height[:i+1])

        for i in range(len(suffix)):
            suffix[i] = max(height[i:])

        for i in range(len(height)):
            water_now = min(prefix[i], suffix[i]) - height[i]
            res += water_now

        return res