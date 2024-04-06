# Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow_node = head
        fast_node = head.next

        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None:
                return None 
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        fast_node = fast_node.next
        min_distance = self.distance(head, slow_node)
        start_node = slow_node  
        
        while fast_node != slow_node:
            distance = self.distance(head, fast_node)
            if distance < min_distance:
                min_distance = distance
                start_node = fast_node
            fast_node = fast_node.next

        return start_node  

        
        
    def distance(self, source: ListNode, dest: ListNode) -> int:
        distance = 0
        while source != dest:
            source = source.next
            distance += 1
        return distance

