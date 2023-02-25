# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set() 
        current = head 
        loop_start = None  
        while current: 
            if current not in seen:
                seen.add(current) 
                current = current.next 
            else: 
                loop_start = current 
                break 
        if loop_start is not None: 
            prev = head 
            current = prev.next 
            while current is not loop_start:
                current = current.next 
                prev = prev.next 
            return current  
        return None  
        