from collections import defaultdict

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    cnt_map = defaultdict(int)
    max_cnt = int(len(nums)//2) + 1
    for n in nums:
      cnt = cnt_map[n] + 1
      if cnt == max_cnt:
        return n
      else:
        cnt_map[n] = cnt
    
if __name__ == "__main__":
  s = Solution()
  nums = [2,2,2]
  print(s.majorityElement(nums))
        