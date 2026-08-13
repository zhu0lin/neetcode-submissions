class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        U:
        input: array of integers heights where heights[i] is
        the height of the ith bar
        output: an integer of the maximum area the container can be
        P:
        Two pointer:
        One at start and one at end
        Calculate area by doing (end-start) * min(heights[end], heights[start])
        If bigger than res, set res to to new area

        """
        res = float('-inf')
        start = 0
        end = len(heights)-1
        while(start < end):
            if (end-start) * min(heights[start], heights[end]) > res:
                res = (end-start) * min(heights[start], heights[end])
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return res 