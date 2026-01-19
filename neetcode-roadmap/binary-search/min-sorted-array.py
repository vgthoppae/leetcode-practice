class Solution:
  def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    answer = -1

    while left <= right:
      mid = left + (right-left)//2
      if nums[left] <= nums[mid]:
        left = mid + 1
      elif nums[mid] <= nums[right]:
        answer = nums[mid]
        right = mid - 1
    return answer

if __name__ == '__main__':
  s = Solution()
  print(s.findMin([4,5,6,7]))          