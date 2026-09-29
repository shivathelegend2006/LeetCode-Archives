# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next

        count = (count // 2 )+ 1
        while count > 1:
            head = head.next
            count -= 1

        return head