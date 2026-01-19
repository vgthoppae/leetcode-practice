class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    parans_map = {
      "(":")", 
      "{":"}",
      "[":"]"
    }
    for _, c in enumerate(s):
      if c in parans_map:
        stack.append(c)
      elif (len(stack) == 0 or
           c != parans_map[stack.pop()]):
        return False

    return len(stack) == 0


if __name__ == '__main__':
  s = Solution()
  s1 = "]"
  print(s.isValid(s1)) 