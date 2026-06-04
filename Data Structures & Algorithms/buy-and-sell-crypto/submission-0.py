class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        best = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                best = max(best, price - lowest)
        return best
