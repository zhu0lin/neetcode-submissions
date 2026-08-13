from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_k = []
        ans = []
        
        i = 0
        for val in sorted(freq.values(), reverse=True):
            if i < k:
                top_k.append(val)
                i += 1
            elif i == k:
                break

        for element in freq:
            if freq[element] in top_k:
                ans.append(element)
                
        
        return ans
