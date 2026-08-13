"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Min-heap to track end times
        heap = []

        # Add the end time of the first meeting
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            # If the room is free (earliest meeting ended)
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)  # reuse that room

            # Allocate new room (or reuse)
            heapq.heappush(heap, intervals[i].end)

        return len(heap)