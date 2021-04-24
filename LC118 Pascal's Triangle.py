def generate(numRows):
    result =[[] for i in range(numRows)]

    for i in range(numRows):
        for j in range(i+1):
            if j < i:
                if j == 0:
                    result[i].append(1)
                else :
                    result[i].append(result[i-1][j] + result[i-1][j-1])

            elif j == i :
                result[i].append(1)
        print(result)





print(generate(5))