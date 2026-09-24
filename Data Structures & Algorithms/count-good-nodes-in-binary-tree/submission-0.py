# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0

        def dfs(root, maxv):
            nonlocal res
            if not root:
                return 

            if root.val>=maxv:
                res+=1

            dfs(root.left, max(root.val,maxv))
            dfs(root.right, max(root.val,maxv))
            return 

        dfs(root, root.val)
        return res

        