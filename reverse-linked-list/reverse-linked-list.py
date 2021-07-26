# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous_node = None
        while head != None:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node