class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-int(n) for n in nums] 
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1 
        return str(-maxHeap[0])
        