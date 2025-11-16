from typing import List
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    minprice = float('inf')
    maxprofit = 0

    for p in prices:
      minprice = min(minprice, p)  # consider today's price if it is minimum
      maxprofit = max(maxprofit, p - minprice)

    return maxprofit
if __name__ == "__main__":
  s= Solution()
  prices = [10,8,7,5,2]
  # prices = [10,1,5,6,7,1]
  print(s.maxProfit(prices))