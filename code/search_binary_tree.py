class Node(object):
    def __init__(self,value,left=None,right=None,tag=0):
        self.value=value
        self.left = left
        self.right = right
        self.tag=tag

class search_binary_tree():
    def __init__(self,value):
        self.root=Node(value=value)

    # 前序遍历的递归写法
    def preorder(self,node):
        if node is not None:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
    # 层序遍历的实现
    def cen_travel(self):
        cen_lst=[self.root]
        while len(cen_lst)!=0:  #此处是两个if可以并行执行
            if cen_lst[0].left is not None:   #依次让队首左右孩子入队
                cen_lst.append(cen_lst[0].left)
            if cen_lst[0].right is not None:
                cen_lst.append(cen_lst[0].right)
            print(cen_lst[0].value)   #打印队首元素 并出队
            del cen_lst[0]

     # 中序遍历实现
    def in_travel(self):
        in_travel_lst = []
        node =self.root
        while len(in_travel_lst)!=0 or node is not None:
            while node is not None and node.tag==0:
                in_travel_lst.append(node)
                node.tag=1
                node=node.left
            else:
                node=in_travel_lst[-1]
                while node.tag==2:
                    if len(in_travel_lst)>=1:
                        in_travel_lst.pop()
                    if len(in_travel_lst)!=0:
                        node=in_travel_lst[-1]
                if node.tag==1:
                    print(node.value)
                    node.tag = 2
                    node=node.right




    def find(self,value):
        node=self.root
        while node is not None: #while里面每个句子是执行一遍还是遍    单一执行还是并行执行
            if value<node.value :  #只能运行一次  不能再一次中多次向下探索
                node=node.left
            elif value>node.value :
                node=node.right
            else:
                return 1
        return -1
    def find_max(self,node):
        while node.right is not None:
            node=node.right
        return node
    def find_min(self):
        while node.left is not None:
            node=node.left
        return node
    def insert(self,value):
        node=self.root
        #找到插入位置
        while node.left is not None and node.right is not None: #while里面每个句子是执行一遍还是遍    单一执行还是并行执行
            if value<node.value :  #只能运行一次  不能再一次中多次向下探索
                node=node.left
            elif value>node.value :
                node=node.right
        # 插入操作
        insert_node=Node(value=value)
        if value<node.value:
            node.left=insert_node
        if value>node.value:
            node.right=insert_node
    def delete(self):
        pass
    def make_empty(self):
        pass
lst=[2,8,1,4,3]
a=search_binary_tree(value=6)
for each in lst:
    a.insert(each)
# a.preorder(a.root)
# print(a.find_max(a.root).value)
# print(a.find(7))
a.in_travel()
