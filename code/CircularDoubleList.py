class Node:
    def __init__(self, value=None, pre=None, next=None):
        self.value, self.pre, self.next = value, pre, next  # 不能这样写self.value,pre,next=value,pre,next


class CircularDoubleList(object):
    def __init__(self):
        self.root = Node(value=None, pre=None, next=None)  # 默认都为None
        self.length = 0

    # 尾插法
    def append_right(self, value):
        if self.root.next ==None:  # 第一个插入情况
            node = Node(value=value, pre=self.root, next=self.root)
            self.root.next = node
            self.root.pre = node
        else:
            node = Node(value=value, pre=self.root.pre, next=self.root)
            self.root.pre.next = node
            self.root.pre = node
        self.length += 1

    # 头插法
    def append_left(self, value):
        if self.root.next ==None:  # 第一个插入情况
            node = Node(value=value, pre=self.root, next=self.root)
            self.root.next = node
            self.root.pre = node
        else:
            node = Node(value=value, pre=self.root, next=self.root.next)
            self.root.next.pre = node
            self.root.next = node
        self.length += 1

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.pre

    def remove(self, node):
        #包含头，尾巴，一般，及数量为一的删除方法
        node.pre.next=node.next
        node.next.pre=node.pre
        del node
        self.length-=1

    def __iter__(self):
        if self.iter_node()==None:
            raise Exception("it is empty")
        else:
            for each in self.iter_node():
                print(each.value,end=" ")
        print('\n')
    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.root:
            yield curnode
            curnode = curnode.next

    def iter_node_reverse(self):
        curnode=self.root.pre
        while curnode is not self.root:
            print(curnode.value,end=' ')
            curnode=curnode.pre


a = CircularDoubleList()
lis = [1, 2, 3, 4, 5,10,9,8,7,6]
for i in range(5):
    a.append_right(lis[i])
for i in range(5,10):
    a.append_left(lis[i])
a.__iter__()
a.remove(a.headnode().next)
a.__iter__()
a.remove(a.tailnode())
a.__iter__()
a.remove(a.headnode())
a.__iter__()
a.iter_node_reverse()
