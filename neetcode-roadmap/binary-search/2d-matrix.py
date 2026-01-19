from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #let's figure out the row where the target could be located
    for row in matrix:
      last_element = row[len(row)-1] 
      if last_element == target:
        return True;
      elif last_element > target:
        ret = self.searchInRow(row, target)
        return ret != -1
      continue
    return False

  def searchInRow(self, nums:List[int], target:int) -> bool:
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
  print(s.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))      
        