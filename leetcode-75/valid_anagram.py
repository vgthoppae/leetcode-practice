class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
  s1= Solution()
  s = "anagram"
  t = "nagaram"
  print(s1.isAnagram(s, t))