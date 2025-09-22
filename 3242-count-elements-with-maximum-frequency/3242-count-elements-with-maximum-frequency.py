class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        r=max(d.values())
        count=0
        for i in d:
            if d[i] == r:
                count+=1
        return count*r

        