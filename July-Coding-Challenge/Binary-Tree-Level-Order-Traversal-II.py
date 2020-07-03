#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        
        q, res = [root], [[root.val]]       # queue will contain the node object
                                            # res will contain the value of the node
        # BFS
        while q:
            parent = q.pop(0)
            children = []
            
            if parent.left:
                children.append(parent.left.val)
                q.append(parent.left)
            if parent.right:
                children.append(parent.right.val)
                q.append(parent.right)
            if len(children): res.append(children)
            
        return res[::-1]    # reverse the elements

sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.levelOrderBottom(root))
