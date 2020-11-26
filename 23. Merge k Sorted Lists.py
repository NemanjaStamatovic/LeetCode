# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        res = []
        
        for i in range(len(lists)):
            while lists[i]:
                res.append(lists[i].val)
                lists[i] = lists[i].next
                
        res.sort()
        
        node_start = node = ListNode()
        
        while res:
            node.next = ListNode(res.pop(0))
            node = node.next
            
        return node_start.next  