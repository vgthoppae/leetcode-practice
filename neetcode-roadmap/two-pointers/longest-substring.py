class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    max_len = 0
    window = set()

    for right, c in enumerate(s):
      while c in window:
        window.remove(s[left])
        left += 1
      window.add(c)
      max_len = max(max_len, len(window))

    return max_len

if __name__ == '__main__':
  s = Solution()
  print(s.lengthOfLongestSubstring("xxxx"))   
        
        