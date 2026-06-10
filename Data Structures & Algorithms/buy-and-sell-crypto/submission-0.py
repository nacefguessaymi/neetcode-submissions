class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i, price in enumerate(prices):
            arr = prices[i:]
            for j in arr:
                if price < j:
                    ans = max(ans, (j - price))
        return ans