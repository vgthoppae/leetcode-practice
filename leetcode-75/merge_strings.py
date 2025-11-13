class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    result = ""

    if (word1 and (not word2 or len(word2) == 0)): return word1
    if (word2 and (not word1 or len(word1) == 0)): return word2

    for i in range(len(word1)):
      result += word1[i]
      if i < len(word2):
        result += word2[i]
      else:
        result += word1[i+1:]
        break

    if i < len(word2) - 1:
      result += word2[i+1:]

    return result;


if __name__ == "__main__":
  s = Solution();
  print (s.mergeAlternately("abc", "pqr"))
  print(s.mergeAlternately("abc", "pq"))
  print(s.mergeAlternately("ab", "pqrs"))
  print(s.mergeAlternately("ab", ""))
  print(s.mergeAlternately("", "c"))