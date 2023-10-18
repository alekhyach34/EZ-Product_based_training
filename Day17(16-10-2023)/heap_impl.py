from heapq import heappop, heapify, heappush, _heapify_max
min_heap=[1,4,2,6]
heappush(min_heap,10)
heapify(min_heap)
e=heappop(min_heap)
e=heappop(min_heap)
print(min_heap)
print("=======")
max_heap=[-1,-4,-2,-6]
heappush(max_heap,-10)
_heapify_max(max_heap)
e=heappop(max_heap)
e=heappop(max_heap)
print(max_heap)
print("======")
