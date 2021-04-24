def isAlienSorted( words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """

    ls = [i for i in order]

    for i in range(len(words) - 1):
        word1,word2 = words[i],words[i+1]
        for j in range(min(len(word1),len(word2))):
            if word1[j] != word2[j]:
                if ls.index(word1[j]) > ls.index(word2[j]):
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False



    return True










print(isAlienSorted(words = ["kuvp","q"], order = "ngxlkthsjuoqcpavbfdermiywz"))