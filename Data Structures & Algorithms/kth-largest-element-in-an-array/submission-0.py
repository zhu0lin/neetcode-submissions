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

        """
        heap = [-n for n in nums]
        heapq.heapify(heap)

        count = 0
        popped = None
        while count < k:
            popped = heapq.heappop(heap)
            count += 1

        return -popped