class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        idx=[]
        for i in range(1,n):
            if sorted(words[i-1]) == sorted(words[i]):
                idx.append(i)
        for i in idx[::-1]:
            words.pop(i)
        return words

