def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    result = [[] for i in range(rowIndex+1)]
    for i in range(rowIndex+1):

        for j in range(i+1):
            if j < i:
                if j == 0:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j] + result[i-1][j-1])



            elif i == j:
                result[i].append(1)
    print(result)
    return(result[-1])

print(getRow(3))