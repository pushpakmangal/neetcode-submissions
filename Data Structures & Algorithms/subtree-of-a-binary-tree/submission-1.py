# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sametree(self, p, q):
        stack=[(p,q)]
        while stack:
            node1,node2=stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val!=node2.val:
                return False
            stack.append([node1.left, node2.left])
            stack.append([node1.right, node2.right])

        return True

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sametree(root,subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
        