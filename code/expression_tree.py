class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left = left
        self.right = right


data_input='ab+cde+**'

nums=['a','b','c','d','e']
operations=['+','*']
def main():
    lst=[]
    for each in data_input:
        if each in nums:
            lst.append(each)
        else:
            node=Node(value=each,left=lst[-2],right=lst[-1])
            lst.pop()
            lst.pop()
            lst.append(node)
main()
