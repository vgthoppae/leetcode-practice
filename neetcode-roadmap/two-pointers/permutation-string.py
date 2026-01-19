from collections import Counter, defaultdict
class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    right= 0
    s1_len= len(s1)
    # s1_cnt = Counter(s1)
    s1_cnt = defaultdict(int)
    for i in range(s1_len):
      s1_cnt[s1[i]] += 1

    for left, c in enumerate(s2):
      if c not in s1:
        continue
      window = defaultdict(int)
      if left+s1_len > len(s2): break
      for right in range(left, left+s1_len):
        window[s2[right]] += 1
      if s1_cnt == window:
        return True
    return False
        
if __name__ == '__main__':
  s = Solution()
  s1 = "abc"
  s2 = "lecabee"
  print(s.checkInclusion(s1, s2))   