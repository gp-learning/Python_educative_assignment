def groupAnagrams( strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # result = {}
    # for word in strs:
    #     a= (''.join(sorted(word)))
    #     if a not in result:
    #         result[a] = [word]
    #     else:
    #         result[a].append(word)
    # print(list(map(sorted, result.values())))
    # return sorted(result.values())

    result={}
    for word in strs:
        a=[0 for i in range(26)]
        for w in word:
            a[ord(w)-ord('a')] += 1


        b = tuple(a)
        if b not in result:
            result[b] = [word]

        else:
            result[b].append(word)
    print(result)
    return result.values()





print(groupAnagrams(strs =["bdddddddddd","bbbbbbbbbbc"]))