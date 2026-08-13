class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap approach
        negated_stones = [-weight for weight in stones]
        heapq.heapify(negated_stones)

        while len(negated_stones) > 1:
            x = -heapq.heappop(negated_stones)
            y = -heapq.heappop(negated_stones)

            if x != y:
                heapq.heappush(negated_stones, -abs(y-x))

        if negated_stones:
            return -negated_stones[0]
        else:
            return 0
            
        