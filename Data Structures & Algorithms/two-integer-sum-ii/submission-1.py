class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        """
        Input: array of integers sorted in non decreasing order
        Output: There will always be exactly one valid solution
        where [i, j] represents numbers[i] + numbers[j] == target and i != j
        Note that the indices are 1 indexed not 0 indexed

        Two pointers approach
        One at the left of numbers, one at the right of numbers
        If numbers[left] + numbers[right] == target, return [left, right]
        Else if numbers[left] + numbers[right] < target, move left forward 
        by one
        Else move right backward by one
        """
        left = 0
        right = len(numbers)-1

        while left != right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
