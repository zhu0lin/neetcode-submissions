class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dic = {}

        # for i in range(len(nums)):
        #     dic[nums[i]] = i

        # for i in range(len(nums)):
        #     if target - nums[i] in dic and i != dic[target - nums[i]]:
        #         return [i, dic[target - nums[i]]]
        """
        Instead of the two pass we have above, we can do one pass.
        We can do this by populating our dic while also checking for 
        if the target - curr_val exists in our dictionary
        """
        dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i] # dic[diff] will always be a smaller index
                # than i, because we've added dic[diff] before we have seen nums[i]!
            dic[nums[i]] = i