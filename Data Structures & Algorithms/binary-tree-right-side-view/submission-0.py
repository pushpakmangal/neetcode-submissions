# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res=[root.val]
        q=deque([root])
        while q:
            tmp=None
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    tmp=node.left.val
                    q.append(node.left)
                if node.right:
                    tmp=node.right.val
                    q.append(node.right)
                
            if tmp is not None:
                res.append(tmp)
        return res
                
                

        