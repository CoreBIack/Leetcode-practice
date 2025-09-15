
def solution(nums):
    
  nums.sort()
  output = []
  numsLength = len(nums)
  for index in range(numsLength):
      if index > 0 and nums[index - 1] == nums[index]:
          continue
      left = index + 1
      right = numsLength - 1 
      while left < right:
          total = nums[index] + nums[left] + nums[right]
          if total == 0:
              output.append([nums[index], nums[left], nums[right]])
              left += 1
              right -= 1
              while left < right and nums[left - 1] == nums[left]:
                  left += 1
              while left < right and nums[right] == nums[right + 1]:
                  right -= 1
          elif total < 0:
              left += 1
          else:
              right -= 1
  return output
print(solution([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))