def twoSumLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    temp =  []
    nums.sort()
    print(nums)
    for i in  range(0,len(nums)):
        for j in range(i+1,len(nums)):
            s = nums[i] + nums[j]
            if s < k :
                temp.append((s))

    return -1 if len(temp) == 0 else  max(temp)

    #     s = nums[i] + nums[i-1]
    #     if s < k:
    #         temp.append(s)
    #
    # return temp[-1] \
        # if len(temp) == 0 else -1


print(twoSumLessThanK(nums = [10,20,30], k = 15))