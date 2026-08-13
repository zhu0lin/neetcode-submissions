import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Understand
        Input: An array piles, where piles[i] represents the number
        of bananas in that pile. An integer h, which represents the 
        hours you need to eat all the bananas within.
        Output: An integer k such that you can eat all the bananas
        within h hours. 

        So basically the smallest k (eating rate) such that you can still 
        finish all the bananas in h hours.

        Plan:
        Start off with k = max(piles)
        Find out total time needed to complete all piles with k 
        eating rate
        """
        k = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            center = (l+r) // 2
            time_to_finish = 0
            for i in range(len(piles)):
                time_to_finish += math.ceil(float(piles[i])/center)
            if time_to_finish <= h:
                k = center
                r = center-1
            else:
                l = center+1

        return k

