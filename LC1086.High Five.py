def highFive( items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    items_dict = {}
    result=[]
    for i in items:
        if i[0] not in items_dict:
            items_dict[i[0]] = [i[1]]
        else:
            items_dict[i[0]].append(i[1])

    print(items_dict)

    for k ,v in items_dict.items():
        print(v)
        v.sort(reverse= True)
        result.append([k,int(sum(v[0:5])/5)])

    print(result)

print(highFive( [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))