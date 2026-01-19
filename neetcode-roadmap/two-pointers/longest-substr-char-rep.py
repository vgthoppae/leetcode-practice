from collections import defaultdict

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    left = max_len = 0
    window = defaultdict(int)
    result = 0
    for left, _ in enumerate(s):
      right = left
      cnt = 0
      while right  < len(s):
        window[s[right]] += 1
        if ((right - left + 1) < k or
           len(window) < k):
          right += 1
          continue
        else: #AABCAD, 2; ABCD, 3
          min_occuring = min(window)
          max_occuring = max(window)
          cnt = 0
          for _,v in window.items():
            if v == window[max_occuring]: 
              continue
            if cnt == k:
              result = window[max_occuring] + cnt
              break
            if v == window[min_occuring]:
              cnt += 1

    return max_len

if __name__ == '__main__':
  s = Solution()
  print(s.characterReplacement("ABBB", 2))         