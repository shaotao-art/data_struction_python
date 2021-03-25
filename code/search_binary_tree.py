class Node(object):
    def __init__(self,value=None,left=None,right=None,tag=0):
        self.value=value
        self.left = left
        self.right = right
        self.tag=tag

class search_binary_tree():
    def __init__(self):
        self.root=Node()

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
            elif value==node.value:
                print(f'找到的节点的值为：{node.value}')
                return node
        print('未找到该节点')
        return -1
    def find_node_and_its_parent(self,value):
        node = self.root
        parent=Node()   #注意如果返回none应该是根节点
        flag=None
        while node is not None:
            if value < node.value:  # 只能运行一次  不能再一次中多次向下探索
                parent=node   #将父亲节点的值保存下来即可
                flag=0         #是左子树返回flag为0
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
                flag = 1
            elif value == node.value:
                print(f'找到的节点的 父亲节点 值为：{parent.value}')
                print(f'找到的节点的值为：{node.value}')
                return parent,node,flag
        print('未找到该节点')
        return -1

    def find_max(self,node):
        while node.right is not None:
            node=node.right
        return node
    def find_min(self,node):
        while node.left is not None:
            node=node.left
        return node
    def insert(self,value):
        # node=self.root
        # #找到插入位置
        # while node.left is not None and node.right is not None: #while里面每个句子是执行一遍还是遍    单一执行还是并行执行
        #     if value<node.value :  #只能运行一次  不能再一次中多次向下探索
        #         node=node.left
        #     elif value>node.value :
        #         node=node.right
        # # 插入操作
        # insert_node=Node(value=value)
        # if value<node.value:
        #     node.left=insert_node
        # if value>node.value:
        #     node.right=insert_node

        #二次改写
        '''
        写好伪代码后，一次成功
        在家写了很多次 才迷迷糊糊的跑通
        由此可见伪代码的重要性
        :param value:
        :return:
        '''
        node = self.root
        if node.value is None:
            self.root.value=value
        else:
            while True:
                if value<node.value and node.left is None:
                    insert_node=Node(value=value)
                    node.left=insert_node
                    break  #插入之后不要忘记break
                elif value>node.value and node.right is None:
                    insert_node = Node(value=value)
                    node.right = insert_node
                    break
                elif value<node.value and node.left is not None:
                    node=node.left
                elif value>node.value and node.right is not None:
                    node=node.right

    def delete(self,value):
        parent,node,flag=self.find_node_and_its_parent(value)  #node为将要删除的节点

        while True:
            if node.left is None and node.right is None:
                if flag==0:
                    parent.left=None
                elif flag==1:
                    parent.right=None
                break
            if node.left is not None and node.right is None:   #只有左节点
                if flag==0:
                    parent.left=node.left
                elif flag==1:
                    parent.right=node.left
                break
            if node.left is None and node.right is not None:  #只有右边节点
                if flag==0:
                    parent.left=node.right
                elif flag==1:
                    parent.right=node.right
                break
            if node.left is not None and node.right is not None:  #同时具有左右子树
                #找出右子树的最小节点
                node_to_delete=self.find_min(node.right)
                temp=node
                #值替换
                parent, node, flag = self.find_node_and_its_parent(node_to_delete.value)
                temp.value = node_to_delete.value
                '''
                node=node_to_delete.value
                parent, node, flag = self.find_node_and_its_parent(node_to_delete.value)
                有错误  因为此时的node.value已经变成了要找的值，所以 下面find_parents找到的也是上层的东西
                '''



lst=[6,2,8,1,5,3,4 ]
a=search_binary_tree()
for each in lst:
    a.insert(each)
a.cen_travel()

