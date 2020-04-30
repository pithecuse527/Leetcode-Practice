#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_lst = ListNode(0)
        walker = res_lst
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carry = 0
            tmp_sum = x + y + walker.val
            walker.val = (tmp_sum % 10)
            
            if tmp_sum >= 10:       # for handling carry
                carry = 1
            
            # moving on
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
            # check if there still need to create new node for the result
            # which means, if there is other numbers need to be added or carry occured
            if carry or l1 or l2:
                walker.next = ListNode(carry)           # pass carry first
                walker = walker.next
            
        return res_lst

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
    l1 = makeTestLst([1])
    l2 = makeTestLst([9,9])
    
    s1 = Solution()
    tmp = s1.addTwoNumbers(l1, l2)
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    