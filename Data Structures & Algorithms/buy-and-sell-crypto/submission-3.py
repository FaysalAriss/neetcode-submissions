class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRight = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            maxRight = max(maxRight, prices[i])
            prices[i] = maxRight-prices[i]

        return max(*prices) if len(prices) >= 2 else prices[0]