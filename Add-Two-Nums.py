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
        
        while l1 and l2:
            carry = 0
            tmp_sum = l1.val + l2.val
            walker.val += (tmp_sum % 10)
            
            if tmp_sum >= 10:       # for handling carry
                carry = 1
            
            if carry == 1 or l1.next or l2.next:        # for different length of nums and if there is carry
                walker.next = ListNode(carry)           # pass carry first
                walker = walker.next

            # moving on
            l1 = l1.next
            l2 = l2.next
            
        # leftovers
        while l1:
            walker.next = ListNode(l1.val)
            walker = walker.next
            l1 = l1.next
        
        while l2:
            walker.next = ListNode(l2.val)
            walker = walker.next
            l2 = l2.next
            
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
    l1 = makeTestLst([3,4,2])
    l2 = makeTestLst([4,6,5])
    l3 = makeTestLst([5])
    l4 = makeTestLst([7])
    
    s1 = Solution()
    tmp = s1.addTwoNumbers(l3, l4)
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    