class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    seen = {}
    maxlength = 0
    length = 0
    print(s)
    for right in range(len(s)):
      if s[right] in seen:
        left = seen[s[right]] + 1
        length = right - left + 1
        del seen[s[right]]
      else:
        length += 1
      seen[s[right]] = right
      maxlength = max(maxlength, length)
      print(f"s[right]-{s[right]};left-{left};right-{right};seen-{seen};length-{length};maxlength-{maxlength}")

    return maxlength;

  # def lengthOfLongestSubstring(self, s: str) -> int:
  #   group=""
  #   maxlength = 0
  #   for c in s:
  #     if c in group:
  #       group=group[group.find(c)+1:]
  #
  #     group += c
  #     length = len(group)
  #     maxlength = max(length, maxlength)
  #
  #   return maxlength

if __name__ == "__main__":
  s1= Solution()
  # s = "pwwkew"
  # s = "zxyzxyz"
  # s = "xxxxx"
  # s = ""
  # s = "restrcrust"
  # s = "abcbde"
  s = "abba"
  print(s1.lengthOfLongestSubstring(s))