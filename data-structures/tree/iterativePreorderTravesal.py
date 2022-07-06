"""
Given a Binary Tree, write an iterative function to print the Preorder traversal of the given binary tree.
Refer to this for recursive preorder traversal of Binary Tree. To convert an inherently recursive procedure to iterative, we need an explicit stack. 

Following is a simple stack based iterative process to print Preorder traversal. 

Create an empty stack nodeStack and push root node to stack. 
Do the following while nodeStack is not empty. 
Pop an item from the stack and print it. 
Push right child of a popped item to stack 
Push left child of a popped item to stack
The right child is pushed before the left child to make sure that the left subtree is processed first.
"""

class Node:
    """A binary tree node"""
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def iterativePreorder(root):
    """
    :param root: root of the tree
    :return: preorder traversal of the tree
    """
    if root is None:
        return []
    nodeStack = []
    nodeStack.append(root)
    result = []
    while len(nodeStack) > 0:
        node = nodeStack.pop()
        result.append(node.data)
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
    return result

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
print(iterativePreorder(root))