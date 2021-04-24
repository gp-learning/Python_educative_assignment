import heapq
def findKthLargest( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # nums.sort()
    #
    # print(nums)
    # return(nums[len(nums)-k])
    heap=[]
    for i in range(len(nums)):
        if i < k :
            heapq.heappush(heap,nums[i])
        elif nums[i] > heap[0]:
            heapq.heappushpop(heap,nums[i])
    return(heap[0])


print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))