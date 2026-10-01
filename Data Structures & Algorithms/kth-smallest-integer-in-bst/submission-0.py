# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestHelper(self, root: Optional[TreeNode], res: List[int]) -> None:
        if not root:
            return
        
        self.kthSmallestHelper(root.left, res)
        res.append(root.val)
        self.kthSmallestHelper(root.right, res)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        self.kthSmallestHelper(root, res)

        return res[k - 1]
        