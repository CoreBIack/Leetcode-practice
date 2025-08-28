def solution(strs):
  anagrams = {}
  for string in strs:
      key = "".join(sorted(string))
      if key not in anagrams:
          anagrams[key] = []
      anagrams[key].append(string)
  return anagrams.values()
print(solution(["eat","tea","tan","ate","nat","bat"]))