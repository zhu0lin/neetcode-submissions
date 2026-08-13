import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Understand
        Input: 
        A 2D array points where points[i] = [x,y] of a pair of
        coordinates. 
        An integer k for the k closest points to the origin (0,0)
        Output: A 2D array with the k closest points to the origin

        Plan
        Approach: Min heap with the distance of each point 
        Iterate over points, add each points distance to heap array
        Heapify the heap array to make it a min heap

        """
        # heap = []
        # for i in range(len(points)):
        #     dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
        #     heap.append([dist, points[i]])

        # heapq.heapify(heap)
        # res = []
        # while len(res) < k:
        #     res.append((heapq.heappop(heap))[1])

        # return res
        heap = []
        for x,y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap) #this will pop off farther points from the heap
        
        return [point for (_, point) in heap]