class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words= text.split(" ")
        count = 0
        for word in words:
            for j in brokenLetters:
                if j in word:
                    count+=1
                    break
        return len(words) - count
                
            
        