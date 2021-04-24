def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # if sorted(s) == sorted(t):
    #     return True
    # else:
    #     return False
    #

    # s_dic = {}
    # t_dic = {}
    #
    # for i in s:
    #     if i not in s_dic:
    #         s_dic[i] =1
    #     else:
    #        s_dic[i]+=1
    #
    # for  j in t:
    #     if j not in t_dic:
    #         t_dic[j] = 1
    #     else:
    #         t_dic[j] +=1
    #
    # print(s_dic,t_dic)
    #
    # if s_dic == t_dic:
    #     return True
    # else:
    #     return False

    w1 = [0]*26
    w2 = [0 for i in range(26)]
    for w in s :
        w1[ord(w)-ord('a')] +=1


    for o in t:
        w2[ord(o)-ord('a')] +=1

    if w1==w2:
        return True

    return False

print(isAnagram(s = "anagrm", t = "nagaram"))
