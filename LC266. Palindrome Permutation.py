def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    res ={}
    cnt=0
    if not s:
        return True
    for char in s :
        if char not in res :
            res[char] = 1
        else:
            res[char] += 1


    for i in res.values():
        if  i%2 !=0:
            cnt+= 1

    if cnt > 1:
        return False
    return True


    # ans = [i%2 for i in res.values()]
    # print(ans)
    # if len(s) % 2 == 0 :
    #     print(set(ans))
    #     if set(ans) == {0}:
    #         return True
    # elif len(s) %2 !=0:
    #     for j in ans:
    #         if j == 1:
    #             cnt+=1
    # if cnt == 1:
    #     return True
    # else:
    #     return False




print(canPermutePalindrome(s = "carerac"))