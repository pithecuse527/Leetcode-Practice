#!/usr/bin/python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseToFindParent(self, root: TreeNode, x: int, loc: int):       # based on pre-order traverse
        if (root.left and root.left.val == x) or (root.right and root.right.val == x) :
            return loc, root
        
        new_loc = loc + 1
        tmp = None
        if root.left:
            tmp = self.traverseToFindParent(root.left, x, new_loc)
            if tmp: return tmp
        if root.right: 
            tmp = self.traverseToFindParent(root.right, x, new_loc)
        return tmp
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        walking_res1 = self.traverseToFindParent(root, x, 0)
        walking_res2 = self.traverseToFindParent(root, y, 0)
        
        if walking_res1 and walking_res2 and walking_res1[0] == walking_res2[0] and walking_res1[1] is not walking_res2[1]:
            return True
        return False
    