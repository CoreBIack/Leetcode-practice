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
"""
prefix = nums[0]
suffix = nums[-1]
rtrn = [1] * len(nums)
for i in range(1, len(nums)):
    rtrn[i] *= prefix 
    prefix *=  nums[i]
    rtrn[-i - 1] *= suffix
    suffix *= nums[-i- 1]
return rtrn
"""