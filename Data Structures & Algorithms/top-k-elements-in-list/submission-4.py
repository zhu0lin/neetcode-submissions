class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        res = []

        while len(res) < k:
            max_val = max(dic.values())
            for val in dic:
                if dic[val] == max_val:
                    res.append(val)
                    del dic[val]
                    break

        return res