# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        #define distance between right pointer and left pointer
        while right and n > 0:
            right = right.next
            n -= 1
        #loop through linked list
        while right:
            left = left.next
            right = right.next
        
        #delete node
        left.next = left.next.next
        return dummy.next

        