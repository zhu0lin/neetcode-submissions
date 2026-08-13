"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Understand
        Input: An array of objects with object.start and object.end times
        Output: True if a person does not have conflicts in their timings.
        i.e. there are never any overlaps of meetings. 
        A meeting with end time == start time of another meeting is not a conflict.

        Plan
        Time complexity should be nlogn so I'm thinking we can sort
        the tuples first by their starting times?
        Start at intervals[1]. 
        Check if intervals[i][0] < intervals[i-1][1]. If it is return False. This is an overlap, which is a conflict.
        Else, continue iterating over the tuples
        """
        if not intervals:
            return True

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i].start < sorted_intervals[i-1].end:
                return False

        return True

        