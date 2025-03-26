# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def p(node):
            if node is None:
                return 
            else:

                r.append(node.val)
                p(node.left)
                p(node.right)
       
        p(root)
        return r
