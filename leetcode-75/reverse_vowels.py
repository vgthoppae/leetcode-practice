class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = set('aeiouAEIOU')
    right = len(s) - 1
    res = [""]*len(s)
    for left in range(len(s)):
      if (left == right):
        res[left] = s[left]
        break
      if s[left] in vowels:
        while True:
          if s[left] == s[right]:
            res[left] = s[left]
            res[right] = s[right]
            right = right - 1
            break
          if s[right] in vowels:
            res[right] = s[left]
            res[left] = s[right]
            right = right - 1
            break
          else:
            res[right] = s[right]
            right = right - 1
            continue
      else:
        res[left] = s[left]
    return ''.join(res)

if __name__ == "__main__":
  s= Solution()
  st = "iat"
  print(s.reverseVowels(st))