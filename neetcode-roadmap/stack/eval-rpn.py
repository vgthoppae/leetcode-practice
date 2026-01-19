class Solution:
  operands = ["+", "-", "*", "/"]

  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for t in tokens:
      if not t in self.operands:
        stack.append(t)
      else:
        b = stack.pop()
        a = stack.pop()
        stack.append(int(eval(f"{a}{t}{b}")))
    return int(stack.pop())
        
if __name__ == '__main__':
  s = Solution()
  tokens = ["4","13","5","/","+"]
  print(s.evalRPN(tokens))         