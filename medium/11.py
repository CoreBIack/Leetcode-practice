def solution(height):
  left = 0
  right = len(height) - 1
  max = -1
  while left < right:
      container = (right - left) * min(height[left], height[right])
      if container > max:
          max = container
      if height[left] < height[right]:
          left += 1
      else:
          right -= 1           
  return max
print(solution([1,8,6,2,5,4,8,3,7]))