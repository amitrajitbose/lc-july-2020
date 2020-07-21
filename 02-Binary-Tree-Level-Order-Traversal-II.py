# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [(root,0)] # queue DS
        while len(q):
            node, lvl = q.pop(0)
            if len(res) < lvl+1:
                res.append([])
            res[lvl].append(node.val)
            if node.left is not None:
                q.append((node.left, lvl+1))
            if node.right is not None:
                q.append((node.right, lvl+1))
        return res[::-1]

"""
Time : O(height of binary tree)
Space: O(number of nodes)
"""

