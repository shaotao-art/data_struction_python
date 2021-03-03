class Node(object):
    def __init__(self,name,frist_child=None,next_brother=None,value=None):
        self.name=name
        self.first_child=frist_child
        self.next_brother=next_brother
        self.value=value


user=Node(name='user',value=1)

mark=Node(name='mark',value=1)
alex=Node(name='alex',value=1)
bill=Node(name='bill',value=1)

book=Node(name='book',value=1)
course1=Node(name='course1',value=1)
junk_c1=Node(name='junk_c1',value=6)
junk_c2=Node(name='junk_c2',value=8)
work=Node(name='work',value=1)
course2=Node(name='course2',value=1)

ch1_r=Node(name='ch1_r',value=3)
ch2_r=Node(name='ch2_r',value=2)
ch3_r=Node(name='ch3_r',value=4)
cop3530=Node(name='cop3530',value=1)
cop3212=Node(name='cop3212',value=1)
fall96_1=Node(name='fall96_1',value=1)
spr97=Node(name='spr97',value=1)
sum97=Node(name='sum97',value=1)
fall96_2=Node(name='fall96_2',value=1)
fall97=Node(name='fall97',value=1)
syl_r1=Node(name='syl_r1',value=1)
syl_r2=Node(name='syl_r2',value=5)
syl_r3=Node(name='syl_r3',value=2)
grades1=Node(name='grades1',value=3)
prog1=Node(name='prog1',value=4)
prog2=Node(name='prog2',value=1)
prog3=Node(name='prog3',value=2)
prog4=Node(name='prog4',value=7)
grades2=Node(name='grades2',value=9)
user.first_child=mark

mark.next_brother=alex
mark.first_child=book
alex.next_brother=bill
alex.first_child=junk_c2
bill.first_child=work

book.first_child=ch1_r
ch1_r.next_brother=ch2_r
ch2_r.next_brother=ch3_r
book.next_brother=course1
course1.next_brother=junk_c1
course1.first_child=cop3530
cop3530.first_child=fall96_1
fall96_1.next_brother=spr97
spr97.next_brother=sum97
fall96_1.first_child=syl_r1
spr97.first_child=syl_r2
sum97.first_child=syl_r3

work.next_brother=course2
course2.first_child=cop3212
cop3212.first_child=fall96_2
fall96_2.next_brother=fall97
fall96_2.first_child=grades1
grades1.next_brother=prog1
prog1.next_brother=prog2

fall97.first_child=prog3
prog3.next_brother=prog4
prog4.next_brother=grades2

#前序遍历的递归写法
def preoder(node):
    if node is not None:
        print(node.name)
        preoder(node.first_child)
        preoder(node.next_brother)



# 用列表模拟栈的非递归写法
def my(node):
    lst = []   #栈的初始化
    depth = -1
    while len(lst) != 0 or node is not None:
        if node is not None:   #对于一个节点如果不是空
            lst.append(node)
            depth=depth+1   #入队
            print('     ' * depth, node.name)#打印
            node =node.first_child#对于任何节点都是先查找其第一个子节点  深度优先
        else:  #运行至此 之前的都是遍历子节点  深度优先   子节点没了 开始兄弟节点  但是一变兄弟节点之后又开始立刻子节点遍历
            node=lst[-1] #先存下栈顶元素的只  因为要node.next_brother
            lst.pop()  #出队
            depth-=1
            node=node.next_brother #遍历兄弟节点



def my1():
    lst = [user]   #栈的初始化
    depth = -1
    node=lst[-1]
    while len(lst) != 0:
        if node is not None:   #对于一个节点如果不是空
            lst.append(node)
            depth=depth+1   #入队
            print('     ' * depth, node.name)#打印
            node =node.first_child#对于任何节点都是先查找其第一个子节点  深度优先
        else:  #运行至此 之前的都是遍历子节点  深度优先   子节点没了 开始兄弟节点  但是一变兄弟节点之后又开始立刻子节点遍历
            node=lst[-1] #先存下栈顶元素的只  因为要node.next_brother
            lst.pop()  #出队
            depth-=1
            node=node.next_brother #遍历兄弟节点


my1()