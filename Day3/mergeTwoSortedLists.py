# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_array = []
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        p1 = l1
        p2 = l2
        
        while p1:
            merged_array.append(p1.val)
            p1 = p1.next
        
        while p2:
            merged_array.append(p2.val)
            p2 = p2.next
            
        merged_array.sort()
        
        current = ll = ListNode(merged_array[0])
        i = 1
        while i < len(merged_array):
            current.next = ListNode(merged_array[i])
            current = current.next
            i += 1
        
        return ll