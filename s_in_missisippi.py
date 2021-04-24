def find_s(str):
    cnt = 0
    for char in str:
        if char == 's':
            cnt+=1
    return None if len(str)== 0  else cnt

print(find_s(''))
