def runningSum( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    total = 0
    for i in nums:
        total = i + total
    return total



print(runningSum(nums = [1,2,3,4]))