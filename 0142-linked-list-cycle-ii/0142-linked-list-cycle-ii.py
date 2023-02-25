# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# coded this one up from my head using common sense in a few minutes 
# while being interrupted at my day job without referring to any 
# external sources... maybe it should be marked "easy", not "medium" level difficulty 
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
        