# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        l2r = True
        if not root:
            return res
        queue = [root]
        while queue:
            lvlSize = len(queue)
            currLvl = []
            for i in range(lvlSize):
                curr = queue.pop(0)
                if l2r:
                    currLvl.append(curr.val)
                else:
                    currLvl.insert(0, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(currLvl)
            l2r = not l2r
        return res

