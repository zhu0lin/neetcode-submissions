class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # lower bound is 1 b/c koko min eating rate is 1
                            # upper bound is max(piles) b/c koko can jus take 
                            # one hour for each pile at that point
        res = max(piles)

        while l <= r:
            eating_rate = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float((pile/eating_rate)))
            if hours <= h:
                res = min(res, eating_rate)
                r = eating_rate - 1 #try getting even smaller eating rate
            else:
                l = eating_rate + 1 #we need a greater eating rate 

        return res