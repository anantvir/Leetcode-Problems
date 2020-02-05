"""Make a Min Heap. Heap stores end times of the intervals. Iterate over the input array and for each element 
check if the root of min heap(smallest element) i.e the earliest end time of any meeting is greater than
the start time of current meeting. If yes, then add a room"""

interval_list = [[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]

import heapq

def MeetingRooms_II(intvl_lst):
    heap = []
    heapq.heappush(heap,intvl_lst[0][1])                # Initialize the heap. Push 1st end time onto heap
    rooms = 1
    for i in range(1,len(intvl_lst)):                   # i = 1 to last element
        if heap:
            earliest_end = heap[0]                      # DONT POP HERE !! just peek the top value
            curr_start_time = intvl_lst[i][0]           # Start time of current meeting
            if earliest_end > curr_start_time:
                rooms += 1
                heapq.heappush(heap,intvl_lst[i][1])    
            else:
                heapq.heappop(heap)                     # Pop from heap only when you know you are going to use the root of heap to assign the room to some other meeting
                heapq.heappush(heap,intvl_lst[i][1])    # Push onto the heap end time of current meeting
        else:
            raise ValueError("Cannot Process Empty Heap !")
    return rooms
        
print(MeetingRooms_II(interval_list))
        


