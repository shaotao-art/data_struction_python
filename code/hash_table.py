'''
前置单下划线
单个下划线是一个Python命名约定，表示这个名称是供内部使用的。
它通常不由Python解释器强制执行，仅仅作为一种对程序员的提示。

后置单下划线
单个末尾下划线（后缀）是一个约定，
用来避免与Python关键字产生命名冲突。 PEP 8解释了这个约定。


我们可以使用“_”来表示它只是一个临时值
'''
class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value



class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None ):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

    def print(self):
        for item in self._items:
            print(item)


lst_test=[41, 59, 100, 62, 24, 45, 72, 52]

class Hash_table():
    UNUSED=None
    DELETED=Slot(None,None)
    #生成空白的哈希表
    def __init__(self,maxsize):
        self.hash_table=Array(size=maxsize)
        self.used=0

    def basic_hash(self,value):
        index=value%self.hash_table._size
        return index


    # 以简单的i%m为哈希函数
    '''
    第一个赋值的时候会将所有的值都赋值  因为所有的数组中的对象指向同一个地址
    '''
    def insert_basic(self,value)->int:
        index=self.basic_hash(value)
        if self.hash_table[index] is not None:
            index=self.solve_confliction(value,index)
            self.hash_table[index]=value
        else:
            self.hash_table[index]=value
        self.used+=1
        return index

    def solve_confliction(self,value,index)->int:
        i=0
        while self.hash_table[index] is not None:
            i=i+1
            index=(index+i*i)%(self.hash_table._size)
        return index


    def find(self,value):
        i=1
        index=self.basic_hash(value)
        while True:
            if self.hash_table[index]==value:
                return index
            elif self.hash_table[index] is self.UNUSED:
                return -1
            else:  #delete 和  正常的往下迭代  都是继续往下面迭代
                index=(index+i*i)%self.hash_table._size
                i+=1


    def remove(self,value):
        index=self.find(value)
        if index==-1:
            print('no such element')
        else:
            self.hash_table[index]=self.DELETED
        self.used-=1

    def rehash(self):
        temp=self.hash_table
        if self.load_factor()>0.75:
            self.hash_table=Array(size=len(self.hash_table)*2)
            self.used=0
            for each in temp:
                if each is not self.UNUSED and each is not self.DELETED:
                    self.insert_basic(each)
        del temp
    def load_factor(self)->int:
        print(f'the load factor is {self.used/self.hash_table._size}')
        return self.used/self.hash_table._size

    def __iter__(self):
        self.hash_table.print()

test=Hash_table(maxsize=13)
for each in lst_test:
    test.insert_basic(each)
test.__iter__()
test.load_factor()
test.insert_basic(13)
test.__iter__()
test.load_factor()
test.insert_basic(9)
test.__iter__()
test.load_factor()
test.rehash()
test.__iter__()
test.load_factor()
