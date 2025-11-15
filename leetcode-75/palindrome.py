class Solution:
  def isPalindrome(self, s: str) -> bool:
    i=0
    j=len(s) - 1
    while i<j:
      if not s[i].isalnum():
        i += 1
        continue
      while i<j:
        if not s[j].isalnum():
          j -= 1
          continue
        if s[i].lower() != s[j].lower():
          return False
        else:
          j -= 1
          break
      i+=1

    return True


if __name__ == "__main__":
  strs =  "tab a cat"
  s = Solution()
  print(s.isPalindrome(strs))

  #p11p!@