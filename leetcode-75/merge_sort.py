from typing import List


class Solution:
  def merge_sort(self, nums: List[int]) -> List[int]:
    if (len(nums) <= 1):
      return nums

    n = len(nums)//2

    left = self.merge_sort(nums[:n])
    right = self.merge_sort(nums[n:])

    return self.merge(left, right)

  def merge(self, left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i<len(left) and j<len(right):
      if left[i] <= right[j]:
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
  s = Solution();
  nums = [5, 1, 4, 2, 8]
  print(s.merge_sort(nums))