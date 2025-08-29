def solution(nums, k):
  numbers = {}
  for num in nums:
      if num in numbers:
          numbers[num] += 1
      else:
          numbers[num] = 1
  highs = []
  for i in range(k):
      high = max(numbers, key=numbers.get)
      highs.append(high)
      numbers[high] = 0
  return highs
print(solution([1,1,1,2,2,3], 2))
""" if key is larger
def topKFrequent(nums, k):
    # 1. Count frequencies
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # 2. Sort by frequency, descending
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # 3. Take top k keys
    return [item[0] for item in sorted_items[:k]]
"""