## Straight and easy answer:
##   return ' '.join(s.split()[::-1])
## I have purposely used two pointers strategy for extra fun

class Solution:
  def reverseWords(self, s: str) -> str:
    words = s.strip().split(" ")

    j = len(words)
    for i in range(len(words)):
      words[i] = words[i].strip()
      if len(words[i]) > 0:
        while j > i:
          j -= 1
          words[j] = words[j].strip()
          if (len(words[j]) > 0):
            tmp = words[i]
            words[i] = words[j]
            words[j] = tmp
            break

      if i >= j:
        break

    res = ""
    for w in words:
      if len(w)>0:
        if len(res) > 0:
          res += " " + w
        else:
          res += w
    return res

if __name__ == "__main__":
  s = Solution()
  st =  " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU"
  print(s.reverseWords(st))