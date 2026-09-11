"""
LeetCode #121: Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Time Complexity: O(n) - single pass through prices
Space Complexity: O(1) - constant extra space
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculate maximum profit from buying and selling stock once.
    
    Args:
        prices: List of stock prices where prices[i] is price on day i
        
    Returns:
        Maximum profit achievable (0 if no profit possible)
    """
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]  # Track minimum price seen so far
    max_profit = 0  # Track maximum profit achievable
    
    for price in prices[1:]:
        # Calculate profit if sold today (current price - min price so far)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
        # Update minimum price seen so far
        min_price = min(min_price, price)
    
    return max_profit

# Alternative approach: track maximum profit ending at each day
def max_profit_dp(prices: List[int]) -> int:
    """
    Dynamic programming approach: max profit ending at day i.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices or len(prices) < 2:
        return 0
    
    # dp[i] represents max profit achievable up to day i
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        # Profit if we sell on day i
        profit_today = prices[i] - min_price
        max_profit = max(max_profit, profit_today)
        
        # Update minimum price for future calculations
        min_price = min(min_price, prices[i])
    
    return max_profit

# Test cases
if __name__ == "__main__":
    # Test case 1: [7,1,5,3,6,4] -> 5 (buy at 1, sell at 6)
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Output: {max_profit(prices1)}")  # Expected: 5
    print()
    
    # Test case 2: [7,6,4,3,1] -> 0 (no profit possible)
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Output: {max_profit(prices2)}")  # Expected: 0
    print()
    
    # Test case 3: [2,4,1] -> 2 (buy at 2, sell at 4)
    prices3 = [2, 4, 1]
    print(f"Input: prices = {prices3}")
    print(f"Output: {max_profit(prices3)}")  # Expected: 2
    print()
    
    # Test case 4: Single price
    prices4 = [5]
    print(f"Input: prices = {prices4}")
    print(f"Output: {max_profit(prices4)}")  # Expected: 0
    print()
    
    # Test case 5: Empty list
    prices5 = []
    print(f"Input: prices = {prices5}")
    print(f"Output: {max_profit(prices5)}")  # Expected: 0
    print()
    
    # Test case 6: All same prices
    prices6 = [3, 3, 3, 3]
    print(f"Input: prices = {prices6}")
    print(f"Output: {max_profit(prices6)}")  # Expected: 0