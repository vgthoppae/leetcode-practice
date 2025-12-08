class Solution:
  def isValid(self, s) -> bool:
    brackets = {
      "{": "}",
      "[": "]",
      "(": ")"
    }
    stack = []
    for c in s:
      if c in brackets.keys():
        stack.append(c)
      elif not stack:
        return False
      else:
        a = stack.pop()
        if a in brackets.keys():
          if brackets[a] == c:
            continue
        return False
    return not stack

if __name__ == "__main__":
  s = Solution()
  print(s.isValid(""))
  # print(s.isValid("()[]{}"))
  # print(s.isValid("([{}])"))
  # print(s.isValid("(]"))
  # print(s.isValid("([)]"))
  # print(s.isValid("((("))
  # print(s.isValid("(}[]"))
  # print(s.isValid("}}}}"))
  # print(s.isValid("[}}}}"))