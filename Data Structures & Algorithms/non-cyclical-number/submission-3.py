class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while(True):
            curr_sum = 0
            while (n > 9):
                curr_sum = curr_sum + ((n % 10) ** 2)
                n = n//10
            curr_sum = curr_sum + ((n % 10) ** 2)
            if curr_sum == 1:
                return True
            if curr_sum in seen:
                return False
            seen.add(curr_sum)
            n = curr_sum