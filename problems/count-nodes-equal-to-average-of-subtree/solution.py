# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0

        def dfs(node):
            if not node:
                return(0,0)

            ls,lc=dfs(node.left)
            rs,rc=dfs(node.right)

            cs=ls+rs+node.val
            cc=lc+rc+1

            if node.val==cs //cc:
                self.count+=1        

            return (cs,cc)    
        dfs(root)
        return self.count    