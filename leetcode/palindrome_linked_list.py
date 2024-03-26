# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev


def print_list(head):
    if head is None:
        return None

    while head is not None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    # make a list 1, 2, 3, 4, 5
    head = ListNode(
        1,
        vl1 := ListNode(2, vl2 := ListNode(3, vl3 := ListNode(4, vl4 := ListNode(5)))),
    )

    s = Solution()
    print_list(s.reverse(head))
