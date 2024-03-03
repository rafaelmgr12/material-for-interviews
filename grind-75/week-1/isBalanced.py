"""
Balanced Binary Tree


Given a binary tree, determine if it is 
height-balanced


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(node):
            """
            Retorna a altura da árvore se balanceada, -1 caso contrário.
            """
            if not node:
                return 0
            
            leftHeight = checkHeight(node.left)
            if leftHeight == -1:
                # Subárvore esquerda não está balanceada
                return -1
            
            rightHeight = checkHeight(node.right)
            if rightHeight == -1:
                # Subárvore direita não está balanceada
                return -1
            
            # Verifica se a diferença de altura é maior que 1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Retorna a altura da árvore
            return max(leftHeight, rightHeight) + 1
    
        return checkHeight(root) != -1