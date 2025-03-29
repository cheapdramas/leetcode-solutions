# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_start = head
        while head:
            if head.next != None and head.val == head.next.val:
                #start looking for an unmatched node
                node: Optional[ListNode] = head.next
                while node:
                    if node.val != head.val:
                        break
                    node = node.next
                head.next = node
            head = head.next
        
        return head_start        
