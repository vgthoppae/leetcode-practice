from typing import List
class Solution:
  delimiter = "|"
  def encode(self, strs: List[str]) -> str:
    es = ""
    for s in strs:
      es += str(len(s)) + Solution.delimiter + s
    return es
  def decode(self, s: str) -> List[str]:
    strs = []
    end = 0
    while end < len(s):
      ds = s.index(Solution.delimiter, end)
      length = int(s[end:ds])
      start = ds+1
      end = start + length
      part = s[start:end]
      strs.append(part)
    return strs

if __name__ == "__main__":
  strs = ["we","abracadabra",":","yes","!@#$%^&*()"]
  # strs = ["neet", "", "code"]
  # strs = []
  # strs = [""]
  s = Solution()
  es = s.encode(strs)
  print(es)
  ds = s.decode(es)
  print(ds)