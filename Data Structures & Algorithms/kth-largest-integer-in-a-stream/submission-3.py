class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) #heapify nums input
        while len(self.heap) > self.k: # make sure we only have k elements in the heap
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # push into heap
        while len(self.heap) > self.k: # make sure we only have k elements in the heap
            heapq.heappop(self.heap)
        return self.heap[0] # the kth largest will be the first element in the heap
