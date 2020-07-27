# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.getIndexOf = {}
        n = len(inorder)
        if n==0:
            return None
        for i in range(n):
            self.getIndexOf[inorder[i]] = i
        pIndex = [n - 1]
        return self.buildUtil(inorder, postorder, 0, n-1, pIndex)
    def buildUtil(self, inorder, postorder, start, end, pIndex):
        if start > end:
            return None
        node = TreeNode(postorder[pIndex[0]])
        pIndex[0] -= 1
        
        if start == end:
            return node
        iIndex = self.getIndexOf[node.val]
        node.right = self.buildUtil(inorder, postorder, iIndex+1, end, pIndex)
        node.left = self.buildUtil(inorder, postorder, start, iIndex-1, pIndex)
        return node

