from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        curr = head.next

        while curr is not None:
            next = curr.next
            curr.next = head
            prev.next = next
            head = curr
            curr = next
            print_list(head)

        return head


def print_list(head: Optional[ListNode]) -> None:
    while head is not None:
        print(head.val)
        head = head.next

    print("\n")


if __name__ == "__main__":
    # make a list node 1, 2 ,3 ,4, 5
    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))),
        ),
    )

    # make a solution
    solution = Solution().reverseList(head)
