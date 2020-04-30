# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_lst = ListNode(0)
        walker = res_lst
        
        while l1 and l2:
            carry = 0
            tmp_sum = l1.val + l2.val + walker.val
            walker.val = (tmp_sum % 10)
            
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
            carry = 0
            tmp_sum = walker.val + l1.val
            walker.val = (tmp_sum % 10)
            
            if tmp_sum >= 10:       # for handling carry
                carry = 1
            
            if l1.next or carry:         # make new node only if there is number which still needs to be added (from l1)
                walker.next = ListNode(carry)
                walker = walker.next
            l1 = l1.next
        
        while l2:
            carry = 0
            tmp_sum = walker.val + l2.val
            walker.val = (tmp_sum % 10)
            