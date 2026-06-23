class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1,len(prices)):
            prof = prices[i] - prices[i-1]
            if prof > 0:
                ans += prof
        return ans