from typing import List
class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    curr_max, curr_min = 0, 0
    global_max, global_min = nums[0], nums[0]
    total = 0

    for n in nums:
      curr_max = max(curr_max, 0) + n
      curr_min = min(curr_min, 0) + n
      global_max = max(global_max, curr_max)
      global_min = min(global_min, curr_min)
      total += n

    return max(global_max, total - global_min) if global_max > 0 else global_max

if __name__ == "__main__":
  s = Solution()
  nums = [5, -1, 5]
  print(s.maxSubarraySumCircular(nums))
