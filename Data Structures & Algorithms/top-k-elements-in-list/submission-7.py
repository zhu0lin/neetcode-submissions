class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # list of empty lists so we can 
                                # append values that appear certain of times later

        for num in nums: 
        # filling up dictionary with frequency of each number
            count[num] = count.get(num, 0) + 1

        for num, frequency in count.items(): 
        # filling up list with nums with frequency corresponding to the list index  
            freq[frequency].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): 
        # start the iteration over the values that appear most
            for num in freq[i]:
                
                res.append(num)
                if len(res) == k:
                    return res

        # return res

        

