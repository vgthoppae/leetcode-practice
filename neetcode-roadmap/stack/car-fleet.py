from collections import defaultdict

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    cars= [(p, s) for p,s in zip(position, speed)]
    cars.sort(reverse=True)
    
    for c in cars:
      rem = target - c[0]
      hrs = rem/c[1]
      stack.append(hrs)
      if len(stack)>1 and stack[-1] <= stack[-2]:
        stack.pop()
      
    return len(stack)
    
if __name__ == '__main__':
  s = Solution()
  target = 12
  position = [10,8,0,5,3]
  speed = [2,4,1,1,3]
  print(s.carFleet(target, position, speed))           