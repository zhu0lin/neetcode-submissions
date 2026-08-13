class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Understand
        Input: An array of integers temperatures where temperatures[i]
        represents the temperature on the ith day
        Output: An array of integers result where result[i] represents
        the number of days until we see a warmer temperature than result[i]

        Plan
        Initialize a stack
        Iterate over the array temperatures 
        Each iteration: check if stack is nonempty and if value >
        the top element on stack
        If it is, pop from the stack, we have found the a greater 
        element than the previous temp. Set the res value for the previous
        temp = current index - previous element index
        Else, add to the stack the current value and it's index
        """
        res = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((value, i))

        return res