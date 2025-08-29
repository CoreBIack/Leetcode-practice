def solution(strs):
  def encode(strs):
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded
  def decode(s):
      decoded = []
      i = 0
      while i < len(s):

          jump = 0

          while s[i] != "#":
              jump += 1
              i += 1
          i -= jump
          decoded.append(s[i + jump + 1:int(s[i:i + jump]) + i + jump + 1])
          i += int(s[i:i + jump]) + jump + 1
      return decoded

  print(encode(strs))
  print(decode(encode(strs)))
print(solution(["we","say",":","yes","!@#$%^&*()"]))