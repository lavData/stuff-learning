# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        interweave = head

        while interweave is not None:
            new_node = Node(interweave.val)
            new_node.next = interweave.next
            interweave.next = new_node
            interweave = new_node.next

        interweave = head
        head = interweave.next

        while interweave is not None:
            if interweave.random is not None:
                interweave.next.random = interweave.random.next
            interweave = interweave.next.next

        interweave = head

        while interweave is not None:
            interweave.next = interweave.next.next if interweave.next else None
            interweave = interweave.next

        return head


# Time complexity: O(N)
