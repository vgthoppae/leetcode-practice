from math import ceil

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    maxp = max(piles)
    left, right = 1, max(piles)
    result = right

    while left <= right:
      mid = left + (right - left)//2
      hours = sum(ceil(i/mid) for i in piles)
      if hours <= h:
        result = mid
        right = mid-1
      else:
        left = mid+1

    return result
    

if __name__ == '__main__':
  s = Solution()
  print(s.minEatingSpeed([25,10,23,4], 4))            