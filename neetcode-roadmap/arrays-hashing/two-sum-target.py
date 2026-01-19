from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    char_cnt_map = {}

    for j in range(len(nums)):
      diff = target - nums[j]
      if diff in char_cnt_map:
        return [char_cnt_map[diff], j]
      else:
        char_cnt_map[nums[j]] = j

if __name__ == '__main__':
  s = Solution()
  print(s.twoSum([3,4,5,6], 7))
