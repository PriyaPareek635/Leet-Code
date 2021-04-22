# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        my_list, ptr = [], head
        while ptr:
            my_list.append(ptr.val)
            ptr = ptr.next
            
        my_list.sort()
        
        ptr = head
        for val in my_list:
            ptr.val = val
            ptr = ptr.next
            
        return head
        
