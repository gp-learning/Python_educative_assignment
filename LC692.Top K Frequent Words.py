import  heapq
def topKFrequent( words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    result = {}
    out=[]
    res=[]
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] +=1

    for key,v in result.items():
        out.append((-v, key))
    print(out)

    heapq.heapify(out)
    for w in range(k):
        res.append(heapq.heappop(out)[1])

    return res


    # for key,v in sorted(result.items(),key =lambda x:x[1],reverse =True)[:k]:
    #     out.append(key)
    # return out


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))