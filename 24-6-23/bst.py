#implementation of single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class bst:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(root,key):
         if root is None:
            return node(key)
         else:
            if root.val==key:
                 return root
            elif root.val <key:
                 root.right=insert(root.right,key)
            else:
              root.left=insert(root.left,key)
         return root
    def append(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def inorder(root):
         if root:
            inorder(root.left)
            print(root.val,end=" ")
            inorder(root.right)
    def search(root,key):
       if root is None or root.val ==key:
           return root
       if root.val <key:
           return search(root.right,key)
       return search(root.left,key)
obj=bst()
n=int(input("how may elements would you like to add"))
for i in range(n):
    data=int(input("enter data items: "))
    obj.append(data)
obj.inorder()

