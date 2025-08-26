def solution(nums, threshold):
  max = 0
  for l in range(len(nums)):
      if (nums[l] % 2 == 0 and nums[l] <= threshold):
          counter = 1
          for r in range(l, len(nums) - 1):
              if (nums[r] % 2 != nums[r + 1] % 2) and nums[r + 1] <= threshold:
                  counter += 1
              else:
                  break
          
          
          if  (max < counter):
              max = counter
  return max
print(solution([3,2,5,4], 4))

"""
ans = 0
        left = 0
        n = len(nums)

        while left < n:
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                right = left

                while right < n and nums[right] <= threshold:
                    if right > left and nums[right-1]%2 == nums[right]%2:
                        break
                    right += 1
                
                ans = max(ans,right-left)
                left = right
            else:
                left += 1
        
        return ans
"""