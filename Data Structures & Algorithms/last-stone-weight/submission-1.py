import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Understand
        Input: An array of integers stones where stones[i] represents
        the weight of the ith stone
        Output: The weight of the last remaining stone or return 0 if
        no stones remain.

        Plan
        Make a heap by heapify stones
        """
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap) 
            y = -heapq.heappop(heap) 

            if x != y:
                heapq.heappush(heap, -(x-y))

        return -heap[0] if heap else 0
                