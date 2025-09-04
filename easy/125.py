def solution(s):
  string = s.lower()

  left = 0
  right = len(s) - 1

  while left < right:
    while not string[left].isalnum() and left < right:
      left += 1
    while not string[right].isalnum() and left < right:
      right -= 1
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1
  return True
print(solution("A man, a plan, a canal: Panama"))

""" preference I think
res = ""

        for char in s:
            if(char.isalnum()):
                res+=char.lower()

        
        left = 0 
        right = len(res)-1 
        
        while left<len(res)//2:
            if(res[left]!=res[right]):
                return False 
            
            left+=1 
            right-=1 
        
        return True"""