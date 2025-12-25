# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            # If current node has duplicates
            if curr.next and curr.val == curr.next.val:
                duplicate_value = curr.val
                # Skip all nodes with this value
                while curr and curr.val == duplicate_value:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next
