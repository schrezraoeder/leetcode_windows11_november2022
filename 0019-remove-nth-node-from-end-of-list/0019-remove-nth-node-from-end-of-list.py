# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-float("inf"), next=head) 
#         current = head.next 
#         prev = dummy 
#         count = 0 
#         [1, 2, 3, 4, 5] n = 2 
#         [1, 2, 3, 5] 
        
#         [dummy, 1, 2, 3, 4, 5] 
#         [dummy, 1, current=2, 3, 4, 5] 
#         [dummy, prev=1, 2, current=3, 4, 5] 
#         [dummy, 1, 2, prev=3, 4, current=5]
#         prev.next = current
#         return dummy.next 
#         while current: 
#             current = current.next 
#             prev = prev.next 
        
        prev = dummy
        current = dummy 
        for i in range(n):
            current = current.next 
        while current.next:
            current = current.next 
            prev = prev.next 
        prev.next = prev.next.next  
        return dummy.next 
        
        
        