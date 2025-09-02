def solution(s):
  string = s.lower()

  left = 0
  right = len(s) - 1

  while left < right:
      while not string[left].isalpha() and left < len(string)/2:
          left += 1
      while not string[right].isalpha() and len(string)/2 < right:
          right -= 1
      if string[left] != string[right]:
          return False
      left += 1
      right -= 1
  return True
print(solution("A man, a plan, a canal: Panama"))