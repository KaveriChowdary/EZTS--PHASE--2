#iterative inorder traversal using list
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    current=root
    stack=[]
    done=0
    while True:
        #reach the left most node of the current
        if current is not None:
            #place pointer to a tree node on the stack
            #before traversing the node's left subtree
            stack.append(current)
            current=current.left
        #backtrack from emptt subtree &visit node
        #at the top of the stack
            #however, if the stack is emptt you are  done
        elif (stack):
            current=stack.pop()
            print(current.data,end= " ")
            current=current.right
        else:
            break
    print()
root=node(100)
root.left=node(400)
root.right=node(500)
root.left.left=node(700)
root.left.right=node(600)
root.left.right.left=node(900)
root.right.left=node(800)
root.right.right=node(200)
root.right.right.left=node(300)
print("in-order")
inorder(root)