from typing import List


class Solution:
  def sort(selfs, nums:List) -> List:
    for i in range(len(nums)):
      min_index = i
      for j in range(i+1, len(nums)):
        if nums[j] < nums[min_index]:
          min_index=j
      nums[i], nums[min_index] =  nums[min_index], nums[i]

    return nums


if __name__ == "__main__":
  s = Solution()
  nums = [5,4,3,2,1]
  print (s.sort(nums))