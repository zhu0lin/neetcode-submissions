class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestSeen = float('inf')
        res = float('-inf')

        for price in prices:
            if price < lowestSeen:
                lowestSeen = price
            else:
                if price - lowestSeen > res:
                    res = price - lowestSeen

        if res < 0:
            return 0
        else:
            return res

