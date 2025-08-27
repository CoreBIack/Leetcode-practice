"""first solution"""
def solution(nums):
    memo = {}
    for num in nums:
        try:
            return memo[num]
        except:
            memo[num] = True
    return False

print(solution([1,2,3,1]))
"""second solution with set for faster checks"""
def solution(nums):
    memo = set()
    for num in nums:
        if num in memo:
            return True
        else:
            memo.add(num)
    return False

print(solution([1,2,3,1]))
"""smart solution"""
def solution(nums):
    return len(nums) != len(set(nums))