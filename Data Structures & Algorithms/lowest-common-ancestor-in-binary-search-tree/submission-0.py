# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        #while curr not null
        while curr:
            #if both bigger than go down right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #if both smaller then go down left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #otherwise you found first node where they seperate so return curr the LCA
            else:
                return curr

        