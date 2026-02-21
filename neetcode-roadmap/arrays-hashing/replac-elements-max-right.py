class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    ret_arr = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
      if i == len(arr) - 1:
        ret_arr[i] = -1
      else:
        ret_arr[i] = max(ret_arr[i+1], arr[i+1])
    return ret_arr
      
if __name__ == "__main__":
  s = Solution()
  nums = [2,4,5,3,1,2]
  print(s.replaceElements(nums))
        