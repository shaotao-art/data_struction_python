## 节点定义
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'node: value={} , next={}'.format({self.value}, {self.next})


## 链表定义
class Link_list(object):

    # 初始化
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()  # python中的变量只是变量  你不知道他要存储的将是什么
        self.tailnode = None
        self.length = 0

    # 返回长度
    def __len__(self):
        return self.length

    # 在链表的尾部插入
    def append_right(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('it is full')
        node = Node(value)
        tailnode = self.tailnode
        # 是否为第一个插入的元素
        if tailnode is None:
            self.root.next = node    # 第一个插入的接在root后
        else:
            tailnode.next = node
        self.tailnode = node  # tailnode是一个节点变量 更新tailnode值
        self.length += 1        #更新length值

    # 在链表的头部插入
    def append_left(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('it is full')
        node = Node(value=value)
        if self.tailnode is None:
            self.tailnode = node
        node.next = self.root.next
        self.root.next = node   #next为node变量
        self.length += 1

    # 重要：迭代器的生成，依次返回每一个节点
    def iter_node(self):
        if self.length == 0:
            print('it is a empty link_list')
        curnode = self.root.next   #产生迭代器的东西本身要是可迭代的
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    # 遍历打印所有节点的值
    def __iter__(self):
        if self.length == 0:
            print('it is a empty link_list')
        else:
            for node in self.iter_node():
                print(node.value, end=' ')
        print('\n')
    # 按值查找   返回其位置 下标从1开始  找不到返回-1
    def find_value(self, value):
        index = 1
        for node in self.iter_node():
            if node.value == value:
                print(index)
                return node
            index += 1
        return -1

    # 按索引查找 返回第i个位置的元素 下标从1开始
    def find_index(self, index):
        if (index > self.length):
            raise Exception('超出链表长度')
        num = 1
        for node in self.iter_node():
            if num == index:
                return node
            num += 1

    # 按值删除
    def remove(self, value):
        prenode = self.root
        if self.length == 0 or self.length == None:
            raise Exception('it is empty,you can not remove.')
        for curnode in self.iter_node():
            if curnode == self.tailnode and curnode.value != value:  # 未找到
                return -1
            elif curnode == self.tailnode and curnode.value == value:  # 删除尾巴节点
                self.tailnode = prenode
                self.length -= 1
                return 1
            elif curnode.value == value:  # 删除头节点 或 中间的任一节点
                prenode.next = curnode.next
                self.length -= 1
                return 1
            else:
                curnode = curnode.next
                prenode = prenode.next

    # 从头部删除元素
    def pop_left(self):
        if self.root.next is None:
            raise Exception('it is empty,you can not pop.')
        elif self.tailnode is self.root.next:  # 链表中只有一个节点的情况
            value = self.tailnode.value
            self.length = 0
            self.root.next = None
            self.tailnode = None
            del self.tailnode
            return value
        else:
            headnode = self.root.next
            self.root.next = headnode.next
            self.length -= 1
            value = headnode.value  # 返回删除节点的值
            del headnode
            return value

    # 从尾部删除元素
    def pop_right(self):
        if self.root.next is None:
            raise Exception('it is empty,you can not pop.')
        elif self.tailnode is self.root.next:  # 链表中只有一个节点的情况
            value = self.tailnode.value
            self.length = 0
            self.root.next = None
            self.tailnode = None
            del self.tailnode
            return value
        else:  # 正常删除及尾巴节点更新
            delnode=self.tailnode
            value = self.tailnode.value
            self.tailnode = self.find_index(self.length-1)
            self.length -= 1
            del delnode
            return value
    # 清空链表
    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None
    #翻转链表
    def revers(self):
        oldhead = self.root.next
        for i in range(self.length-1):
            node=oldhead.next
            oldhead.next=node.next
            self.append_left(node.value)
        self.tailnode=oldhead





a = Link_list()
a.append_right(1)
a.append_right(2)
a.append_right(3)
a.append_right(4)
a.append_right(5)
a.append_right(6)
a.append_right(7)
a.append_right(8)
a.__iter__()
print(a.length)
a.append_left(10)
a.__iter__()
print(a.find_index(1))
print(a.find_index(3))
print(a.find_index(9))
print('a.find6',a.find_value(6))
print(a.find_value(10))
print(a.find_value(8))
a.remove(10)
a.remove(7)
a.remove(8)
print(a.length)
a.__iter__()
a.pop_left()
a.__iter__()
print(a.length)
a.pop_right()
a.__iter__()
a.pop_right()
a.__iter__()
a.revers()
a.__iter__()
a.clear()
a.__iter__()
