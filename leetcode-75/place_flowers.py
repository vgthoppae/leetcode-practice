from typing import List
class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if n == 0: return True

    cnt = 0
    i = 0

    while (i < len(flowerbed)):
      left = False
      right = False

      if (i == 0 or
         flowerbed[i-1] == 0):
        left = True

      if (i == len(flowerbed)-1 or
          flowerbed[i + 1] == 0):
        right = True

      if (left and
        flowerbed[i] == 0 and
        right):
        flowerbed[i] == 1
        i += 2
        cnt += 1
      else:
        i += 1

      if (cnt >= n):
        return True

    return False

if __name__ == "__main__":
  s= Solution()
  flowerbed = [1]
  n = 2
  print(s.canPlaceFlowers(flowerbed, n))