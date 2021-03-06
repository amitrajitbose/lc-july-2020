# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import itertools
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = [(root, 0)] # the tuple keeps track of the node and its index in that level of the tree
        maximum = 1
        
        while level:
            maximum = max(maximum, level[-1][1] - level[0][1] + 1)
            new_level = []
            for node, place in level:
                if node.left: new_level.append((node.left, 2*place + 1))
                if node.right: new_level.append((node.right, 2*place + 2))
            level = new_level
            
        return maximum

