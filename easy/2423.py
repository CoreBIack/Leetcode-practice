word = "abcc"
letters = {}
for letter in word:
  if letter in letters:
    letters[letter] += 1
  else:
    letters[letter] = 1
print(letters)
for letter in letters:
  letters[letter] -= 1
  if letters[letter] == 0:
    letters.pop(letter)
  if len(set(letters.values())) == 1:
    print(True)
  if (letter not in letters):
    letters[letter] = 1
print(False)