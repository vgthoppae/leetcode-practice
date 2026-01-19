class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
      while stack and t>stack[-1][1]:
        j, _ = stack.pop()
        result[j] = i - j
      stack.append((i,t))
    return result
      
if __name__ == '__main__':
  s = Solution()
  temperatures = [22,21,20]
  print(s.dailyTemperatures(temperatures))   
        