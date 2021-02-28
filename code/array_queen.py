class array_queen(object):
    def __init__(self,maxsize):
        self._item=[None]*maxsize
        self.maxsize=maxsize
        self.head=0  #head索引处不存储东西
        self.tail=0  #tail索引处存储东西
        self.length=0

    def is_full(self):
        if self.length+1==self.maxsize:
            print('it has been full')
            return 1    #记得要写返回值  不然返回None则判断不生效

    def is_empty(self):
        if (self.tail)%self.maxsize ==self.head%self.maxsize:
            print('it is empty')
            return 1

    def push(self,value):
        if self.is_full():
            print("full,can not push")
        else:
            self.tail=(self.tail+1)%self.maxsize
            self._item[self.tail]=value
            self.length+=1

    def pop(self):
        if self.is_empty():
            print("empty,can not pop")
        else:
            self.head = (self.head + 1) % self.maxsize
            self._item[self.head] = None
            self.length -= 1
    def __iter__(self):
        for each in self._item:
            print(each,end=' ')
        print('\n')


a=array_queen(5)
b=[12,13,14,15]
for each in b:
    a.push(each)
a.__iter__()
a.pop()
a.__iter__()
a.push(1)
a.__iter__()
a.push(2)
a.__iter__()
for i in range(5):
    a.pop()
a.pop()