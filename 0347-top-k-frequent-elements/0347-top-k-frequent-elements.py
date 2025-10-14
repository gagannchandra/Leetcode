class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_key(d,value):
            for k, v in d.items():
                if v == value:
                    return k

        ans = []
        d = Counter(nums)
        for i in range(k):
            key = get_key(d,max(d.values()))
            ans.append(key)
            del d[key]
        return ans




        