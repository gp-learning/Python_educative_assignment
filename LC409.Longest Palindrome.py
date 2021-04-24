from collections import Counter
def longestPalindrome( s):
    """
    :type s: str
    :rtype: int
    """
    res = {}
    ans=[]
    out=[]
    x=0
    y=0

    for i in s :
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    su = 0
    for val in res.values():
        if val %2== 0:
            su+= val
        else:
            su = su+(val-1)


    if len(s) > su:
        return  su+1
    else:
        return su


print(longestPalindrome(s = "bananas"))