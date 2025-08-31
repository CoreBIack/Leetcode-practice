def solution(nums):
  nums.sort()
  longest = 1
  counter = 1     
  if 1 < len(nums):
      for i in range(len(nums) - 1):
          if nums[i] + 1 == nums[i + 1]:
              counter += 1
          elif nums[i] == nums[i + 1]:
              continue
          else:
              if longest <= counter:
                  longest = counter
              counter = 1
      if longest <= counter:
          longest = counter 
      
      return longest
  elif len(nums) == 1:
      return 1
  return 0
print(solution([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))