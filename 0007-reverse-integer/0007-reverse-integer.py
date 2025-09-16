class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x>0 else -1
        num = abs(x)
        num = str(num)[::-1]
        x = int(num) * flag
        return x if (x < (2**31 - 1) and x > (-2**31)) else 0


        
        