def ascending(nums):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True
def solution(nums):

    for index in range(len(nums)):
        temp_array = nums[:index] + nums[index + 1:]
        if ascending(temp_array):
            return True
    return False 

print(solution([2, 1, 3]))
"""
def canBeIncreasing(self, nums):
        deleted = 0
        for i in range(len(nums)):
            if i >= 1 and nums[i] <= nums[i - 1]:
                if deleted:
                    return False
                if i >= 2 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1] 
                    deleted = 1
                else:
                    nums[i - 1] = nums[i] 
                    deleted = 1
        return True
"""