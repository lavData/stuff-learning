# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    size_list = 0
    current_node = head

    while current_node is not None:
        current_node = current_node.next
        size_list += 1

    current_node = head

    if n > size_list:
        return None
    while size_list - n > 1:
        current_node = current_node.next
        n += 1

    if current_node.next is None:
        return None

    current_node.next = current_node.next.next

    return head


if __name__ == "__main__":
    head = ListNode(
        val=1,
        # next=None,
        next=ListNode(val=2),
        # next=ListNode(
        #     val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))
        # ),
    )

    removeNthFromEnd(head, 2)

    node = head

    while node is not None:
        print(node.val)
        node = node.next
