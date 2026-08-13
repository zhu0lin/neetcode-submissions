class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Input: An array of integers heights where heights[i] is the height of 
        the ith bar
        Output: An integer representing the greatest area that can be created
        with the heights array.
        To get the greatest area, we should be looking for two large
        heights and also how far these two heights are from each other

        Approach: two pointer
        I think we should loop over height and have our pointer
        pointing to the end of the array 
        """
        left = 0
        right = len(heights)-1
        max_area = float('-inf')

        while left < right:

            height = min(heights[left], heights[right])
            width = right - left
            max_area = max(max_area, height * width)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
