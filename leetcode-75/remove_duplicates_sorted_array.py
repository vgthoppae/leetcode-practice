from typing import List
class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i, j = 0, len(nums) - 1
    while i<j:
      if nums[i] == nums[i+1]:
        nums.pop(i)
        j = len(nums) - 1
      elif nums[j] == nums[j-1]:
        nums.pop(j)
        i += 1
      else:
        i += 1
        j -= 1

    return len(nums)


if __name__ == "__main__":
  s = Solution()
  numbers = [2,10,10,30,30,30]
  print(s.removeDuplicates(numbers))