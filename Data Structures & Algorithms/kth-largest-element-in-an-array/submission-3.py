import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Understand
        Input: An unsorted array of integers nums and an integer k.
        Output: The kth largest element in the array nums. This element
        is not the kth distinct element. 

        Plan
        Max heap approach
        Create max heap on nums
        Iterate over the heap until we reach the kth largest element
        Pop off elements in the heap during each iteration
        """
        heap = nums[:k] # first half of the array
        heapq.heapify(heap)

        for num in nums[k:]: # second half of the array
            if num > heap[0]: # we see a larger value
                heapq.heappop(heap) # pop off heap[0]
                heapq.heappush(heap, num) # add this larger value to heap. this automatically places this new larger value into the correct position b/c of heappush property 

        return heap[0]