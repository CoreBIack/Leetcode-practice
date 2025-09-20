def solution(s):
    
  """
  :type s: str
  :rtype: int
  dvdfcgdvrgmnd

  chars = {}
  start = 0
  longest = 0
  length = 0
  trap = -1
  while((trap != len(s)-1) and s):
      for i in range(start, len(s)):
          trap = i
          if s[i] in chars:
              length = i - start
              if longest < length:
                  longest = length
              start = chars[s[i]] + 1
              chars = {}
              break
          chars[s[i]] = i
  if len(s) == len(chars):
      return len(s)
  if len(chars) > 0 and (chars[s[-1]] == len(s) - start):
      return chars[s[-1]]
  return longest
  """
  start = longest = length = 0
  chars = []
  for i in range(len(s)):
      while s[i] in chars:
          chars.remove(s[start])
          start += 1
          
      chars.append(s[i])
      longest = max(longest, i - start + 1)
  return longest

print(solution("pwwkew"))
        