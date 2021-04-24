def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1


    for k,v in result.items():
        if v == 1:
            return(s.index(k))
            break
    return -1






print(firstUniqChar(s = "loveleetcode"))