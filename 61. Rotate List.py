# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None:
            return head
        temp = head
        count = 0
        while temp.next != None:
            count += 1
            temp = temp.next  
        k = k % (count + 1) 
        
        for _ in range(k):
            temp = head

            while temp.next.next != None:
                temp = temp.next

            head1 = temp.next
            head1.next = head
            temp.next = None
            head = head1
      
        return head