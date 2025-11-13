from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    result = [0] * length
    before = [0] * length
    after = [0] * length

    before[0] = 1
    for i in range(1, length):
      before[i] = before[i-1] * nums[i-1]

    after[length-1] = 1
    result[length - 1] = after[length-1] * before[length-1]
    for i in range(length-2, -1, -1):
      after[i] = after[i+1] * nums[i+1]
      result[i] = before[i] * after[i]

    return result


if __name__ == "__main__":
  s = Solution()
  nums = [-1,1,0,-3,3]
  print(s.productExceptSelf(nums))
