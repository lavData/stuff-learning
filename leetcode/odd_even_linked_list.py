from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

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

    s = Solution()
    s.oddEvenList(head)

    print_list(head)
