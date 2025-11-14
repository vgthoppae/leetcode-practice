from typing import List
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    kmap = {}
    for n in nums:
      kmap[n] = kmap.get(n, 0) + 1

    cnt_num_arr = [[] for _ in range(len(nums) + 1)] #plus 1 is needed because we needed as many numbers as in the original array
    for num, cnt in kmap.items():
      cnt_num_arr[cnt].append(num)

    result = []
    for i in range(len(cnt_num_arr)-1, 0, -1):
      if len(cnt_num_arr[i]) > 0:
        result.extend(cnt_num_arr[i])
        if len(result) == k:
          return result
    return result


if __name__ == "__main__":
  s = Solution()
  nums = [7,7]
  k = 1
  print(s.topKFrequent(nums, k))
