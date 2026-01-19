def lengthOfLongestSubstring(s: str) -> int:
  seen = set()
  left = 0
  best = 0

  for right in range(len(s)):
    ch = s[right]

    # shrink window until no duplicate
    while ch in seen:
      seen.remove(s[left])
      left += 1

    # now it's safe to add the new char
    seen.add(ch)
    best = max(best, right - left + 1)

  return best


s = "pwwkew"
print(lengthOfLongestSubstring(s))
