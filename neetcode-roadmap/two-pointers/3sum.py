from collections import defaultdict
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    left, right = 0, len(nums)-1
    while left < right:
      bal = (nums[left] + nums[right]) * -1
      if bal > nums[right]:
        continue
      elif nums[left] < bal < nums[right]:
      


    # result = []
    # nmap = defaultdict(list)

    # for i, num in enumerate(nums):
    #   nmap[num].append(i)

    # left = 0
    # while left<len(nums)-1:
    #   right = left + 1
    #   while right<len(nums):
    #     bal = nums[left] + nums[right]
    #     if -bal in nmap:
    #       third = [x for x in nmap[-bal] if x not in [left, right]]
    #       if len(third)>0:
    #         a = [nums[left], nums[right], -bal]
    #         if not any(sorted(a) == sorted(x) for x in result):
    #           result.append(a)
    #     right += 1
    #   left += 1
    # return result

if __name__ == '__main__':
  s = Solution()
  # print(s.threeSum([-1,0,1,2,-1,-4]))  
  print(s.threeSum([3,0,-2,-1,1,2]))