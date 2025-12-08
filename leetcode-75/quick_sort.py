from typing import List


class Solution:
#   def quick_sort(self, nums: List[int] ) -> List[int]:
#     if len(nums) <= 1:
#       return nums
#
#     pivot = nums[len(nums)//2]
#     left = []
#     right = []
#     for _,n in enumerate(nums):
#       if n < pivot:
#         left.append(n)
#       elif n > pivot:
#         right.append(n)
#
#     L = self.quick_sort(left)
#     R = self.quick_sort(right)
#     L.append(pivot)
#     L.extend(R)
#     return L

  # Implementation of QuickSort
  def quick_sort(self, arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
      return arr

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
      if arr[i] < pivot:
        tmp = arr[left]
        arr[left] = arr[i]
        arr[i] = tmp
        left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    self.quick_sort(arr, s, left - 1)

    # Quick sort right side
    self.quick_sort(arr, left + 1, e)

    return arr



if __name__ == "__main__":
  s = Solution();
  nums = [5, 1, 4, 2, 8]
  print(s.quick_sort(nums, 0, 2))