def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    result = {}
    final_result = []


    for i in range(len(nums)):

        if nums[i] not in result:
            result[nums[i]] = 1
        else:
            result[nums[i]] += 1

    for key,v in (sorted(result.items(), key = lambda x : x[1], reverse=True)[:k]):
        final_result.append(key)

    return final_result





print(topKFrequent(nums = [3,0,1,0], k = 1))
