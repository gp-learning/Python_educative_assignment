def findDuplicate( nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # nums.sort()
    # print(nums)
    # for i in range(1,len(nums)):
    #     if nums[i] == nums[i-1]:
    #         return nums[i]


    seen = set()
    for  i in nums:
        if i in seen:
            return i
        else :
            seen.add(i)

print(findDuplicate(nums = [1,3,4,2,2]))
