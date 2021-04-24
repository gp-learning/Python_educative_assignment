def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    res = []
    for i in nums:
        res.append(i*i)


    res.sort()
    return res
print(sortedSquares(nums = [-4,-1,0,3,10]))