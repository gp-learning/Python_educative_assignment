# replace none with previous values
def replace_none(lst):
    temp = None
    res =[]
    for i in lst:
        if i is not None:
            temp = i
            res.append(i)
        else:
            res.append(temp)
    return None if temp is None else res






print(replace_none([None, 0, 1, 2, None, 3, None, 4]))
print(replace_none([None, None, 1, 2, None, None, 3, None, None, 4,None]))
print(replace_none([None]))
print(replace_none([None, None]))
print(replace_none([1,None, None]))
print(replace_none([]))
print(replace_none([1,2,3]))
print(replace_none([1,2]))
print(replace_none(['',1,2]))





def replace_none(lst):
    temp = None
    result = []
    for i in lst:
        if i is not None:
            temp = i
            result.append(i)
        if i is None:
            result.append(temp)
    return None if temp is None else result


print(replace_none([None, 0, 1, 2, None, 3, None, 4]))
print(replace_none([None, None, 1, 2, None, None, 3, None, None, 4,None]))
print(replace_none([None]))
print(replace_none([None, None]))
print(replace_none([1,None, None]))
print(replace_none([]))
print(replace_none([1,2,3]))
print(replace_none([1,2]))
print(replace_none(['',1,2]))