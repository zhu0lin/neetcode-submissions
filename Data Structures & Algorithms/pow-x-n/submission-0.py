class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Understand
        Input: A floating point value x. An integer value n.
        Output: The floating point value which is x^n

        Plan
        Brute force?:
        Keep multiplying x by itself with a while loop

        """
        res = x
        count = 1
        
        if n == 0:
            return 1
        if n > 0:
            while count < n:
                res *= x
                count += 1
            return res
        else:
            while count != n:
                res *= (1/x)
                count -= 1
            return res