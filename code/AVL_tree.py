class Node(object):
    def __init__(self,value=None,left=None,right=None,tag=0):
        self.value=value
        self.left = left
        self.right = right
        self.tag=tag
        self.depth=0
        self.balance_factor=0


class AVL_tree():
    def __init__(self):
        self.root=Node()

    def get_depth(self,node):
        if node is None:
            return 0
        else:
            return max(self.get_depth(node.left),self.get_depth(node.right))+1
    def single_rotation_left(self, root,parent):
        #下部的旋转
        Y=root.left.right
        K1=root.left
        K1.right=root
        root.left=Y
        #连接母节点
        #设计self.root的旋转  应将新根节点更新self.root 否则树就没了
        if parent:
            if root.value<parent.value:#root为母节点的左孩子
                parent.left=K1
            else:
                parent.right=K1
        else:
            self.root=K1
        #旋转后更新balance_factor depth 值
        K1.depth += 1
        K1.balance_factor=0
        root.balance_factor=0
    def single_rotation_right(self, root,parent):
        # 下部的旋转
        Y = root.right.left
        K1 = root.right
        K1.left = root
        root.right = Y
        # 连接母节点
        if parent:
            if root.value < parent.value:  # root为母节点的左孩子
                parent.left = K1
            else:
                parent.right = K1
        else:
            self.root=K1
        K1.depth+=1
        K1.balance_factor = 0
        root.balance_factor = 0
    def double_rotation_left(self,root,parent):
        parent1=root
        root1=root.left
        self.single_rotation_right(root1,parent1)
        self.single_rotation_left(root,parent)

    def double_rotation_right(self,root,parent):
        parent1 = root
        root1 = root.right
        self.single_rotation_left(root1, parent1)
        self.single_rotation_right(root, parent)
    def check_balance(self,father_lst,value):
        root=None
        parent=None
        father_lst=list(reversed(father_lst))
        #找出最小不平衡子树 及其 父节点
        for each in father_lst:
            if abs(each.balance_factor)>1:
                root=each
                #因为root没有母节点 所以root!=self.root
                #如果是母节点要旋转 就没有母节点
                if root==self.root:
                    pass
                else:
                    parent = father_lst[father_lst.index(each) + 1]  # 要考虑只有一个元素时
        #如果没有不平衡节点就直接完成
        if root==None:
            return -1
        if root.balance_factor==2:# 说明节点被插入左子树
            if value<root.left.value:#说明被插入左子树的左边
                self.single_rotation_left(root,parent)
            else:
                self.double_rotation_left(root,parent)
        elif root.balance_factor==-2:
            if value<root.left.value:#说明被插入左子树的左边
                self.single_rotation_right(root,parent)
            else:
                self.double_rotation_right(root,parent)





    def insert(self,value):
        if self.root.value is None:
            self.root=Node(value=value)
            self.root.depth=1
        else:
            node=self.root
            father_lst=[]
            while node is not None:
                if value<node.value:
                    father_lst.append(node)
                    node=node.left
                else:
                    father_lst.append(node)
                    node=node.right
            #node 为将要插入元素的父亲节点
            node=father_lst[-1]
            if node.left is None and node.right is None:#父亲节点的没有孩子，则要插入元素的所有父亲节点深度都要加一
                #插入
                new_node=Node(value=value)
                new_node.depth+=1
                if value<node.value:
                    node.left=new_node
                else:
                    node.right=new_node
                #更改深度
                for each in father_lst:
                    each.depth+=1
            else:#父亲节点有一个孩子，则要插入元素的所有父亲节点深度不变
                #插入
                new_node=Node(value=value)
                new_node.depth+=1
                if value<node.value:
                    node.left=new_node
                else:
                    node.right=new_node
            # 插入后计算平衡因子
            for each in father_lst:
                if each.left is not None and each.right is not None:
                    each.balance_factor = each.left.depth - each.right.depth
                elif each.left is None and each.right is not None:
                    each.balance_factor = -each.right.depth
                if each.left is not None and each.right is None:
                    each.balance_factor = each.left.depth
                if each.left is None and each.right is None:
                    each.balance_factor = 0
            self.check_balance(father_lst,value)


    # 层序遍历的实现
    def cen_travel(self):
        cen_lst=[self.root]
        while len(cen_lst)!=0:  #此处是两个if可以并行执行
            if cen_lst[0].left is not None:   #依次让队首左右孩子入队
                cen_lst.append(cen_lst[0].left)
            if cen_lst[0].right is not None:
                cen_lst.append(cen_lst[0].right)
            print(f'value={cen_lst[0].value}    ；depth={cen_lst[0].depth}  balance_factor={cen_lst[0].balance_factor}')   #打印队首元素 并出队
            del cen_lst[0]



a=AVL_tree()
lst=[6,2,8,1,5,3,4,7]
for each in lst:
    a.insert(each)
    a.cen_travel()
    print('------------------------------------------------------')
