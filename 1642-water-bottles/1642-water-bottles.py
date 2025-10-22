class Solution:
    def numWaterBottles(self, num: int, k: int) -> int:
        ans = num

        while (num >= k):
            q = num // k
            rem = num - (q*k)
            num = q+rem
            ans += q
        return ans
        