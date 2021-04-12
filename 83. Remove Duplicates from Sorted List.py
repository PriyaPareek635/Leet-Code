# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        tmp=head
        while head.next is not None:
            if(head.val != head.next.val):
                head = head.next
            else:
                head.next=head.next.next
        return tmp
        
