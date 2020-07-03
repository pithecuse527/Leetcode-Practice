# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root: return None
        
        q, res = [root], [[root.val]]           # queue will contain the node object
                                                # res will contain the value of the node
        # BFS
        while q:
            next_level = []     # contains next level nodes' value from s
            next_q = []         # next queue to be used
            
            # dealing general binary tree
            while q:
                s = q.pop(0)
                if s.left:
                    next_level.append(s.left.val)
                    next_q.append(s.left)
                if s.right:
                    next_level.append(s.right.val)
                    next_q.append(s.right)
            q = next_q
            if len(next_level): res.append(next_level)
        
        return res[::-1]    # reverse the elements

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(sol.levelOrderBottom(root))
