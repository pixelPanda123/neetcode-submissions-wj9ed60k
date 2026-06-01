# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        total = 0 
        while curr: 
            curr = curr.next 
            total+=1 
        target = total - n 
        if target == 0: 
            return head.next
        new = head
        i = 0
        while i < target-1: 
            i +=1 
            new = new.next 
            
        new.next = new.next.next 
        return head 


