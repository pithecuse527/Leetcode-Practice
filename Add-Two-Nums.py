#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = 0
        
#         while l1 or l2:
        

def makeTestLst(lst):
    res_lst = ListNode(None)
    walker = res_lst
    for i in range(len(lst) - 1):
        walker.val = lst.pop()
        walker.next = ListNode(None)
        walker = walker.next
    walker.val = lst.pop()
    
    return res_lst

if __name__ == "__main__":
    l1 = makeTestLst([3,4,2])
    l2 = makeTestLst([4,6,5])
    l3 = makeTestLst([5])
    l4 = makeTestLst([5])
    
    
    