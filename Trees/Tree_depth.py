# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def maxDepth(self, root):
        if(root.left == None and root.right == None):
            return 0  
        if(root.left != None):
            ans = 1 + self.maxDepth(root.left)
        if(root.right != None):
            ans2 = 1 + self.maxDepth(root.right)

        return max(ans, ans2)


