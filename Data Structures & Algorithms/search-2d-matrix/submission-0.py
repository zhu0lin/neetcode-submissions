class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # left, right = (0, 0), (len(matrix), len(matrix[0]))

        # while left[0] <= right[0] and left[1] <= right[1]:
        #     middle = ((right[0] - left[0]) // 2, (right[1] - left[1]) // 2)
        #     if matrix[middle[0]][middle[1]] == target:
        #         return True
        #     elif matrix[middle[0]][middle[1]] < target:
        #         if middle[1] == len(matrix[0]) - 1:
        #             left = (middle[0] + 1, 0)
        #         else:
        #             left = (middle[0] + 1, middle[1] + 1)
        #     else:
        #         if middle[1] == 0:
        #             right = (middle[0] - 1, len(matrix[0]))
        #         else:
        #             right = (middle[0] - 1, middle[1] - 1)

        # return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
