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
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]