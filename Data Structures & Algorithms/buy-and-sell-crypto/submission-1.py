class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Understand:
        Input: An array of integers prices, where price[i] is the 
        price of stock on the ith day. 
        Output: An integer that represents the max profit one can make
        from buying at a day and selling at a later day. If no profit 
        can be made, return 0

        Plan:
        Sliding window
        Iterate over the prices array. Check if 
        """
        res = float('-inf')

        for i in range(len(prices)):
            if max(prices[i::]) - prices[i] > res:
                res = max(prices[i::]) - prices[i]

        return res if res > 0 else 0
