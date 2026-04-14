# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        dym = []
        for l in lists: 
            while l: 
                dym.append(l.val)
                l = l.next 
        dym.sort()
        for node in dym: 
            curr.next = ListNode(node)
            curr  = curr.next 
        return dummy.next 
