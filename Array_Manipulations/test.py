import heapq

heap = []

heapq.heappush(heap,44)
heapq.heappush(heap,30)
heapq.heappush(heap,50)
heapq.heappush(heap,22)
heapq.heappush(heap,60)
heapq.heappush(heap,55)
heapq.heappush(heap,77)
heapq.heappush(heap,55)

print(heapq.heappop(heap))
print(heapq.heappop(heap))