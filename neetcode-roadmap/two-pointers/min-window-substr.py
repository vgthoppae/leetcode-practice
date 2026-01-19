from collections implement defaultdict

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if len(t) > len(s): return ""
    t_cnt = defaultdict(int)
    for i in range(len(t)):
      t_cnt[i] += 1
    
    for left, c in enumerate(s):
      if c not in t: continue
      window_cnt = defaultdict(int)
      



if __name__ == '__main__':
  s = Solution()
  s = "OUZODYXAZV"
  s = "XYZ"
  print(s.minWindow(s, t))    
        