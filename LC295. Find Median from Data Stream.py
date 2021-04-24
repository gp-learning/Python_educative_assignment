class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.result = []
        self.l = int(len(self.result)/2)


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num:
            self.result.append(0)
        else:
            self.result.append(num[0])
        self.result.sort()
        self.l = int(len(self.result)/2)



    def findMedian(self):
        """
        :rtype: float
        """
        print(self.result)
        print(self.l)
        if not self.result:
            return 0
        elif len(self.result) % 2 == 0:
            print(self.result[self.l])
            return (self.result[self.l] + self.result[self.l-1]/2)
        else:
            l = int(len(self.result)/2)
            return self.result[self.l]






# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum([])
obj.addNum([])
obj.addNum([1])
obj.addNum([])
obj.addNum([3])
obj.addNum([])

# obj.addNum(1)
# obj.addNum(2)
# obj.addNum(3)
# obj.addNum(4)

print(obj.findMedian())