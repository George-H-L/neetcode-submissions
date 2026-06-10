class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]   # negate -> min-heap acts as max-heap
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)   # largest
            second = -heapq.heappop(heap)  # second largest
            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0