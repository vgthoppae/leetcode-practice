from typing import List
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
      if numbers[left] + numbers[right] > target:
        right -= 1
      elif numbers[left] + numbers[right] < target:
        left += 1
      else:
        return [left + 1, right + 1] #since 1-indexed response is requested

if __name__ == "__main__":
  s = Solution()
  numbers = [2, 3, 4]
  target = 6
  print(s.twoSum(numbers, target))
