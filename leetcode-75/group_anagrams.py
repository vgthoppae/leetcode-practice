from typing import List
from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
      sortedS = ''.join(sorted(s))
      res[sortedS].append(s)
    return list(res.values())

if __name__ == "__main__":
  s= Solution()
  strs = ["act","pots","tops","cat","stop","hat","tah","x"]
  print(s.groupAnagrams(strs))