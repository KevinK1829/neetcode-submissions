# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #store it
            temp = curr.next
            #point to prev node flip arrow
            curr.next = prev
            #update prev to current node since current node will act as new previous node
            prev = curr
            #pull back the temp varibale update curr to temp for the next step   
            curr = temp
        return prev
            

        