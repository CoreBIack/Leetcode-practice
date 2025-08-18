def solution(money, children):
  if (money < children):
      return -1
  money = money - children
  sevens = int(money / 7)
  if sevens == 0:
      return 0
  if (sevens > children):
      return children -1
  elif (sevens == children):
      if(money % 7 != 0):
        return children -1
      return children
  else:
      if (children - sevens == 1 and money % 7 == 3):
          return sevens - 1
      return sevens
print(solution(17,2))