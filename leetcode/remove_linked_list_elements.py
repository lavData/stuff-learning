from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)

        node = head.next
        prev = head
        while node is not None and node.val != val:
            prev = node
            node = node.next

        if node is not None and node.val == val:
            prev.next = self.removeElements(node.next, val)

        return head


def print_list(head):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    # make a list 1, 2, 3, 4, 5
    head = ListNode(
        1,
        vl1 := ListNode(2, vl2 := ListNode(3, vl3 := ListNode(4, vl4 := ListNode(5)))),
    )

    # remove 3
    s = Solution()
    s.removeElements(head, 3)

    print_list(head)
