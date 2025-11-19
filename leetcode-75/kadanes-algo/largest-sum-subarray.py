from typing import List

class Solution:
  def largestSum(self, nums: List[int]) -> int:
    currsum = 0
    maxsum = nums[0]

    for n in nums:
      currsum = max(currsum, 0)
      currsum += n
      maxsum = max(maxsum, currsum)

    return maxsum

if __name__ == "__main__":
  s= Solution()
  nums = [4, -1, 2, -7, 3, 4]
  print(s.largestSum(nums))