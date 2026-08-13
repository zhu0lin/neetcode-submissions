class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Understand 
        Input: A positive integer n.
        Output: True if the sum of the squares of the digits in n
        eventually equals 1. False otherwise.

        Plan:
        Initialize a set seen to track integers, prevents infinite loop
        Use a while loop to modify n 
        How to modify n? 
        Check if n == 1 or if n might be in seen
        """
        seen = set()

        while(True):
            curr_sum = 0
            while(n > 9):
                curr_sum = curr_sum + ((n % 10) ** 2)
                n = n // 10
            curr_sum = curr_sum + ((n % 10) ** 2)
            if curr_sum == 1:
                return True
            if curr_sum in seen:
                return False
            seen.add(curr_sum)
            n = curr_sum



