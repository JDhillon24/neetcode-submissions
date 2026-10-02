# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        count = 1
        def dfs(root):
            if not root:
                return 0
            
            nonlocal count

            left = dfs(root.left)
            right = dfs(root.right)

            count = 1 + max(left, right)
            return count
            

        return dfs(root)