from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0

        for price in prices:
            if price < min_price: # min_price = min(min_price, price)
                min_price = price
            else:
                profit = price - min_price
                res = max(res, profit)
        return res