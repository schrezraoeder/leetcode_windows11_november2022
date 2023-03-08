# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists) 
        pointers = [lists[i] for i in range(k)] 
        answer = None 
        while any(pointers):
            min_val = float('inf')
            for i in range(k):
                if pointers[i]: # assuming node.next == None for end of list, thanks leetcode 
                    # print ()
                    # print ('pointers[i]')
                    # print (pointers[i])
                    if pointers[i].val < min_val:
                        min_val = pointers[i].val 
                        increment_val_pointer = pointers[i] 
                        increment_pointer = i 
                # else:
                #     pointers[i] = False # change from None to False ? 
            if not answer:
                answer = increment_val_pointer 
                head = increment_val_pointer
                pointers[increment_pointer] = pointers[increment_pointer].next  
            else:
                answer.next = increment_val_pointer
                answer = answer.next 
                pointers[increment_pointer] = pointers[increment_pointer].next 
        #answer.next = None 
        if not answer:
            return answer 
        return head 
            
                    
            
        