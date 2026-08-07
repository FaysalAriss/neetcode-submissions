class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, price in enumerate(prices):
            maxPrice = max(*prices[i::], price)
            maxProfit = max(maxPrice-price, maxProfit)

        return maxProfit