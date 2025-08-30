def solution(nums):
  prefixs = [1] * len(nums) 
  suffixs = [1] * len(nums)
  for i in range(1, len(nums)):
      prefixs[i] = prefixs[i - 1] * nums[i - 1]
      suffixs[-i - 1] = suffixs[-i] * nums[-i]
  
  rtrn = []
  for j in range(len(nums)):
      rtrn.append(prefixs[j] * suffixs[j])
  return rtrn
print(solution([1, 2, 3, 4]))