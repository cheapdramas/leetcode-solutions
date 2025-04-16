class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        result = ListNode()
        dummy = result
        counter = 1
        stack = [] 

        while head is not None or head is None:
            if head is None or counter > right:
                stack.reverse()
                for i in stack:
                    dummy.next = i
                    dummy = dummy.next
                dummy.next = head
                dummy = dummy.next
                break
            
            if counter < left:
                dummy.next = head
                dummy = dummy.next
            elif counter >= left and counter <= right:
                stack.append(head)

            counter += 1
            head = head.next 
        return result.next
