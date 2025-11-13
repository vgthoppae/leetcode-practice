class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1.startswith(str2):
      shrt = str2
      lng = str1
    elif str2.startswith(str1):
      shrt = str1
      lng = str2
    else:
      return ""

    while True:
      if lng[:len(shrt)].startswith(shrt):
        lng= lng[len(shrt):]
      else:
        return ""

    d = shrt
    h = len(d)//2
    while True:
      if d[0:h] == d[h:]:
        d = d[h:]
        h = len(d)//2
      else:
        break

    return shrt

if __name__ == "__main__":
  s = Solution();
  print(s.gcdOfStrings("ABABAB", "ABAB"))