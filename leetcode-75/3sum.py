from typing import List
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(nums)):
      j = i + 1
      for k in range(j, len(nums)):
        if (nums[i] + nums[j] + nums[k] == 0):
          res.append([nums[i], nums[j], nums[k]])

    unique = {tuple(sorted(x)) for x in res}
    unique = [list(t) for t in unique]

    return unique

if __name__ == "__main__":
  nums = [-2,0,1,1,2]
  s = Solution()
  print(s.threeSum(nums))

  #p11p!@