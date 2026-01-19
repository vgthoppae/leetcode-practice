from typing import List
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left<=right:
      m = left + (right - left)//2
      if nums[m] == target:
        return m
      elif target> nums[m]:
        left = m+1
      else:
        right = m-1

    return -1

if __name__ == '__main__':
  s = Solution()
  print(s.search([-1,0,2,4,6,8], 4))    