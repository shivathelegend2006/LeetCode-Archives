# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        prev = dummy
        curr = head

        while curr and curr.next:
            second = curr.next
            pair = curr.next.next

            second.next = curr
            curr.next = pair
            prev.next = second

            prev = curr
            curr = pair 

        return dummy.next