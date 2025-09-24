class Solution:
    def maxDifference(self, s: str) -> int:
        d=Counter(s)
        odd = 0
        even = len(s)
        for i in d.values():
            if i % 2 :
                odd =max(odd,i)
            elif i != 0:
                even =min(even,i)

        return (odd-even)