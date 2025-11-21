from typing import List
class Solution:
  def maxArea(self, heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_vol = 0

    while left < right:
      w = right - left
      h = min(heights[left], heights[right])
      max_vol = max(max_vol, w*h)
      if heights[left] < heights[right]:
        left += 1
      else:
        right -=1

    return max_vol


if __name__ == "__main__":
  s= Solution()
  heights = [2,2,2]
  print(s.maxArea(heights))
