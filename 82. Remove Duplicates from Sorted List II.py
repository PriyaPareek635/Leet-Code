# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = dump = ListNode(-1, head)
        while cur and cur.next:
            dup = cur.next #check the repeat node
            while dup.next and dup.val == dup.next.val:
                dup = dup.next
            if cur.next!= dup:
                cur.next = dup.next
            else:
                cur = cur.next
        return dump.next
        
