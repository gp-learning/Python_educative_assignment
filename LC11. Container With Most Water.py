def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l = 0
    r = len(height)-1

    while l <= r :
        print(l,r,height[l],height[r])
        maxarea = max(maxarea,(min(height[l],height[r])* (r-l)))
        print(maxarea)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r-=1
        else:
            l+=1
            r-=1
    return maxarea




print(maxArea(height = [1,3,2,5,25,24,5]))
