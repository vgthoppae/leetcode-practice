from typing import List

class Solution:
  def sort(selfs, nums:List) -> List:
    n = len(nums)
    for i in range(n):
      swapped = False
      for j in range(0, n-i-1):
        if nums[j+1] < nums[j]:
          nums[j],nums[j+1]=nums[j+1],nums[j]
          swapped = True

      if not swapped:
        break

    return nums


if __name__ == "__main__":
  s = Solution()
  nums = [5,4,3,2,1]
  print (s.sort(nums))