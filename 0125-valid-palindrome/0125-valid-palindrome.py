class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i.isalpha()or i.isdigit():
                arr.append(i.lower())
        return True if arr == arr[::-1] else False       