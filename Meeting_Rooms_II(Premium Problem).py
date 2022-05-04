from heapq import *
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x:x.start)
        min_heap=[]
        count=0
        for time in intervals:
            if(len(min_heap)==0):
                count+=1
                heappush(min_heap,(time.end,time.start))
            elif (time.start < min_heap[0][0]):
                count+=1
                heappush(min_heap,(time.end,time.start))
            else:
                heappush(min_heap,(time.end,time.start))
                heappop(min_heap)
        return len(min_heap)
