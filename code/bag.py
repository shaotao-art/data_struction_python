'''
抽象数据类型 ADT Abstract Data Type
'''

class Bag(object):
    def __init__(self , maxsize=10):
        self.maxsize=maxsize
        self._items=list()

    def add(self, item):
        if len(self)>=self.maxsize:
            raise Exception('full')
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)


    # 迭代器iter 与 生成器yield
    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(2)

    assert len(bag)==2

    for i in bag:
        print(i)

'''
__name__为内置函数：
    如果再自己本身的内部：则print(__name__)的值为‘__main__’
    如果被导入到其他的文件：则print(modulename.__name__)的值为模块名

作用：
    模块被导入时会自动运行其中的代码，如果在模块A中，我们有部分的代码不想在被导入到B时直接被运行，但在直接运行A时可直接运行，那该怎么做呢？
    就把这些代码放入到if __name__=='__main__':之下
'''
if __name__=='__main__':
    test_bag()