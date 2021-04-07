# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ptr = ListNode(0)
        head = ptr
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = ListNode(l1.val)
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
                ptr = ptr.next
                
        while l1:
            ptr.next = ListNode(l1.val)
            l1 = l1.next
            ptr = ptr.next
            
        while l2:
            ptr.next = ListNode(l2.val)
            l2 = l2.next
            ptr = ptr.next
            
        return head.next

        
        
