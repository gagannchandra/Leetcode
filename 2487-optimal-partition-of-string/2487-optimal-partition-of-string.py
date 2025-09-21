class Solution:
    def partitionString(self, s: str) -> int:
        temp=''
        count=0
        for i in s:
            if i not in temp:
                temp+=i
            else:
                count+=1
                temp=i
            print(temp)
        return count+1
        