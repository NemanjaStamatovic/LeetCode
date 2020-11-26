# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        val = l1.val + l2.val + carry
        carry = val // 10
        result = ListNode(val % 10)
        if (l1.next or l2.next or carry):
            if not l1.next:
                l1.next = ListNode()
            if l2.next == None:
                l2.next = ListNode()
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return result   
      