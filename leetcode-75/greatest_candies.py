from typing import List
class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    current_max = max(candies)

    result = []
    for i in range(len(candies)):
      if candies[i] + extraCandies >= current_max:
        result.append(True)
      else:
        result.append(False)
    return result


if __name__ == "__main__":
  s = Solution();
  candies = [12,1,12]
  extraCandies = 10
  print(s.kidsWithCandies(candies, extraCandies))