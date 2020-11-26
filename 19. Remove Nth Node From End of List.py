# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        node = ListNode()
        node.next = head
        first = node
        second = node
        
        for _ in range(n):
            first = first.next
            
        while first.next:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return node.next