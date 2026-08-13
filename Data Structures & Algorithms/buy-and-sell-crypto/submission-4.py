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
        Sliding window approach
        left starts at 0th index, r at 1st index
        curr_max starts at 0
        check if prices[l] < prices[r], if it is, calculate and check if 
        the profit is larger than curr_max
        if prices[l] < prices[r] not true, move left forward

        move right forward in each iteration
        """
        l, r = 0, 1
        curr_max = 0

        while(r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                curr_max = max(curr_max, profit)
            else:
                l = r
            r += 1

        return curr_max 
