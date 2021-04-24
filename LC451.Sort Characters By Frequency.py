def frequencySort( s):
    """
    :type s: str
    :rtype: str
    """
    res = {}
    out = ''
    for char in s :
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1

    for k,v in sorted(res.items(),key = lambda x:x[1], reverse= True):
       out += (k*v)

    return out



print(frequencySort("tree"))


