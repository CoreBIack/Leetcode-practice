def solution(prices):
    
  lowest = 0
  highest = 0
  maxProfit = 0
  for i in range(len(prices)):
      if prices[i] < prices[lowest]:
          lowest = i
          highest = lowest
      if i > lowest and prices[i] > prices[highest]:
          highest = i
      if prices[highest] - prices[lowest] > maxProfit:
              maxProfit = prices[highest] - prices[lowest] 
  return maxProfit 

            
print(solution([2,4,1]))