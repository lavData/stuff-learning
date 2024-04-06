from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def print_list(head):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    # make two lists 1, 2, 4 and 1, 3, 4
    list1 = ListNode(
        1,
        vl1 := ListNode(2, vl2 := ListNode(4)),
    )
    list2 = ListNode(
        1,
        vl1 := ListNode(3, vl2 := ListNode(4)),
    )

    s = Solution()
    print_list(s.mergeTwoLists(list1, list2))
