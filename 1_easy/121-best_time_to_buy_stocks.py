from typing import List


class Solution:
    """2 pointer: TOO LONG"""
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit


class Solution:
    """Wrong approach"""
    def maxProfit(self, prices: List[int]) -> int:
        min_price = min(prices)
        min_ix = prices.index(min_price)
        max_price = max(prices[min_ix+1:])
        return max_price - min_price


class Solution:
    """TOO LONG"""
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = []
        for i in range(len(prices)-1):
            max_profits.append(max(prices[i+1:]) - prices[0])
        return max(max_profits)


class Solution:
    """TOO LONG"""
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 9999999
        for i in range(len(prices)-1):
            if prices[i] >= min_price:
                continue
            max_price = max(prices[i+1:])
            if max_price - prices[i] > max_profit:
                max_profit =  max_price - prices[i]
        return max_profit


class Solution:
    """TOO LONG"""
    def maxProfit(self, prices: List[int]) -> int:
        max_price_value = max(prices[1:])
        max_price_ix = prices.index(max_price_value)
        max_profit = 0

        while max_price_ix < len(prices) - 1:
            max_profit_ = max_price_value - min(prices[:max_price_ix])
            if max_profit_ > max_profit:
                max_profit = max_profit_
            max_price_value = max(prices[max_price_ix+1:])
            max_price_ix = prices.index(max_price_value)

        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy

        return max_profit

# PERFORMANCE
# Runtime 686 ms (Beats 90.75% of users with Python)
# Memory 27.40 MB (Beats Beats 33.98% of users with Python)


if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
