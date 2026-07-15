"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         if not intervals: return 0

#         intervals.sort(key=lambda x: x.start)

#         heap = []

#         heapq.heappush((heap, intervals[0][1]))

#         for start, end in intervals[1:]:
#             if start >= heap[0]:
#                 heapq.heappop(heap)
            
#             heapq.heappush(heap, end)
#         return len(heap)
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)