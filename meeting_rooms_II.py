from heapq import *
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x[0])
    min_heap=[]
    count=0
    for time in intervals:
        if(len(min_heap)==0):
            count+=1
            heappush(min_heap,(time[1],time[0]))
        elif (time[0] < min_heap[0][0]):
            count+=1
            heappush(min_heap,(time[1],time[0]))
        else:
            heappush(min_heap,(time[1],time[0]))
            heappop(min_heap)
    return len(min_heap)

intervals=[(0,30),(5,10),(15,20)]
print("Total no. of Rooms : ",minMeetingRooms(intervals))