import re
def solution(sentence):
    count = 0
    words = sentence.split(" ")
    for word in words:
        word = word.strip()
        if len(word) > 0:
            if re.match(r"^[a-z]+-[a-z]$", word):
                count += 1
            elif re.match(r"^[a-z]+[!?,.;:'\"()\[\]{}]$", word):
                count += 1
            elif re.match(r"^([a-z]+)?([a-z]+-[a-z]+)?([!?,.;:'\"()\[\]{}])?$", word):
                count += 1
    return count

print(solution("!this  1-s b8d!"))

"""
pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[,.!]?$')
word_count = 0
for word in sentence.split():
    if pattern.match(word):
        word_count += 1

return word_count
"""