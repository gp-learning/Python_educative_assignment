import heapq

class Solution:
    def __init__(self,nums,k):
        self.heap = []
        self.k = k
        self.nums =nums



    def findKthLargest(self,nums,k):

        for i in range(len(self.nums)):
            if i < self.k:
                heapq.heappush(self.heap,self.nums[i])
            elif self.nums[i] > self.heap[0]:
                heapq.heappushpop(self.heap,self.nums[i])

    def add(self,val):
        if len(self.heap) < self.k :
            self.heap.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap,val)
        print(self.heap)
        return self.heap[0]





my_instance = Solution([4, 5, 8, 3],3)
my_instance.findKthLargest([4, 5, 8, 3],3)
print(my_instance.add(3))
print(my_instance.add(5))
print(my_instance.add(10))
print(my_instance.add(9))
print(my_instance.add(4))
