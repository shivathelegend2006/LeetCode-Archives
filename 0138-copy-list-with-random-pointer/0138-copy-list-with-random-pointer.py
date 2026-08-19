"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #simple hash simple

        if not head: return None

        hash = {None:None}
        curr = head
        while curr:
            hash[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = hash[curr]
            clone.next = hash[curr.next]
            clone.random = hash[curr.random]
            curr = curr.next

        return hash[head]