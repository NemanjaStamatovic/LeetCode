# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        node_start = node = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
                
            node = node.next
            
        node.next = l1 or l2
        
        return node_start.next
        
#         node = ListNode()
#         node_start = ListNode()
        
#         node_start.next = node
        
#         if l1 == None and l2 == None:
#             return node.next
        
#         while l1 and l2:          
#             if l1.val < l2.val:
#                 node.next = ListNode(l1.val)
#                 node = node.next

#                 l1 = l1.next
                
#             else:
#                 node.next = ListNode(l2.val)
#                 node = node.next

#                 l2 = l2.next
            
#         while l1:
#             node.next = ListNode(l1.val)
#             node = node.next
            
#             l1 = l1.next

#         while l2:
#             node.next = ListNode(l2.val)
#             node = node.next
            
#             l2 = l2.next 
     
#         return node_start.next.next