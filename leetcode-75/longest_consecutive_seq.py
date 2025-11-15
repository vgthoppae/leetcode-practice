from typing import List
from collections import defaultdict
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numset = set(nums)
    longest = 0

    for num in numset:
      if num-1 in numset: continue #skip if there is left neighbor
      length= 1
      while (num+length) in numset:
        length += 1
      longest = max(length, longest)

    return longest

if __name__ == "__main__":
  nums = [0,3,2,5,4,6,1,1]
  s = Solution()
  print(s.longestConsecutive(nums))