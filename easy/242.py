def solution(s, t):
  if len(s) != len(t):
    return False

  chars = list(s)
  for i in range(len(s)):
      try:
          chars.remove(t[i])
      except:
          return False


  if len(chars) == 0:
      return True
  return False

print(solution("anagram", "nagaram"))

""" .count()
if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        else:
            return True
"""