"""
Using Morris Traversal, we can traverse the tree without using stack and recursion. 
The idea of Morris Traversal is based on Threaded Binary Tree. 
n this traversal, we first create links to Inorder successor and print the data using these 
links, and finally revert the changes to restore original tree. 

1. Initialize current as root 
2. While current is not NULL
   If the current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Find rightmost node in current left subtree OR
              node whose right child == current.
         If we found right child == current
             a) Update the right child as NULL of that node whose right child is current
             b) Print current’s data
             c) Go to the right, i.e. current = current->right
         Else
             a) Make current as the right child of that rightmost 
                node we found; and 
             b) Go to this left child, i.e., current = current->left
Although the tree is modified through the traversal, it is reverted back to its original shape after the completion. Unlike Stack based traversal, no extra space is required for this traversal.
"""
# Python program to do Morris inOrder Traversal:
# inorder traversal without recursion and without stack


class Node:
  """A binary tree node"""

  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


def morris_traversal(root):
  """Generator function for
  iterative inorder tree traversal"""

  current = root

  while current is not None:

    if current.left is None:
      yield current.data
      current = current.right
    else:

      # Find the inorder
      # predecessor of current
      pre = current.left
      while pre.right is not None and pre.right is not current:
        pre = pre.right

      if pre.right is None:

        # Make current as right
        # child of its inorder predecessor
        pre.right = current
        current = current.left

      else:
        # Revert the changes made
        # in the 'if' part to restore the
        # original tree. i.e., fix
        # the right child of predecessor
        pre.right = None
        yield current.data
        current = current.right


# Driver code
"""
Constructed binary tree is
      1
    / \
    2   3
  / \
  4   5
"""
root = Node(1,
      right=Node(3),
      left=Node(2,
          left=Node(4),
          right=Node(5)
          )
      )

for v in morris_traversal(root):
  print(v, end=' ')

# This code is contributed by Naveen Aili
# updated by Elazar Gershuni
