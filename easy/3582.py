def solution(caption):
  def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        words = caption.strip().split(" ")
        ans = "#" + words[0].strip().lower()

        for i in range(1, len(words)):
            ans += words[i].strip().capitalize()
        
        return ans[:100]
print(solution(" fPysaRtLQLiMKVvRhMkkDLNedQKffPnCjbITBTOVhoVjiKbfSawvpisDaNzXJctQkn"))

"""words = caption.title().split()
        if not words: return "#"
        words[0] = words[0].lower()
        return '#' + ''.join(words)[:99]"""