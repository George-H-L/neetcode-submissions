class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # intiiliase a heap, and k as member variable 

        self.minHeap, self.k = nums, k 

        #make min heap
        heapq.heapify(self.minHeap)

        #while theres more than k values in the list,pop values
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #push values too heap
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


