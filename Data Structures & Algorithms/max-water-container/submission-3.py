class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        front = 0
        back = len(heights) - 1

        # where would be put our two ptrs?
        while front < back:
            water = (back - front) * min(heights[front], heights[back])
            res = max(res, water)

            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1

        return res