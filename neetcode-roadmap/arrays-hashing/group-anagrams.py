from collections import Counter

class Solution:
  def alpha_index(char):
    return ord(char) - ord('a')

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    element = [0] * 26
    char_cnt = [element] * len(strs)
    
    for s in strs:
      for c in s:
        alpha_index(c)
      

    pass
        

if __name__ == '__main__':
  s = Solution()
  print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))        