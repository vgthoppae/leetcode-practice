from typing import List

class Solution:
  def indexLargestSum(self, nums: List[int]) ->tuple[int]:
    currsum = 0
    maxsum = nums[0]
    L = 0
    maxL, maxR = 0, 0

    for R in range(len(nums)):
      if currsum < 0:
        currsum = 0
        L = R
      currsum += nums[R]
      if currsum > maxsum:
        maxsum = currsum
        maxL = L
        maxR = R

    return (maxL, maxR)

if __name__ == "__main__":
  s= Solution()
  nums = [4, -1, 2, -7, 3, 4]
  print(s.indexLargestSum(nums))