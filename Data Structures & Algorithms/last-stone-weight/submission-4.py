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
        Make a max heap to heapify stones
        x = heaviest stone, y = 2nd heaviest stone. Can be vice versa, doesnt matter.
        If x != y, then the stone of weight is x destroyed, but we already
        destroyed it with heappop. y was popped too, so we add it back
        with value -(abs(y-x))
        """
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap) 
            y = -heapq.heappop(heap) 

            if x != y:
                heapq.heappush(heap, -(abs(y-x)))

        return -heap[0] if heap else 0
                