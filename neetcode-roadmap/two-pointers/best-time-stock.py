from typing import List
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    left, right = 0, 1
    max_profit = 0

    while right<len(prices):
      if prices[left] > prices[right]:
        left = right
      else:
        profit = prices[right] - prices[left]
        max_profit = max(profit, max_profit)

      right += 1

    return max_profit

if __name__ == '__main__':
  s = Solution()
  print(s.maxProfit([10,8,7,5,2]))   
        