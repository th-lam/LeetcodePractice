"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

"""
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        lPointer = rPointer = head
        count = 1
        isFirstRun = True
        prevLPointer = None

        while rPointer.next is not None:
            rPointer = rPointer.next
            count += 1

            if count == k:
                tempHead = lPointer

                for i in range(k-1):
                    prevHead = tempHead
                    tempHead = lPointer.next
                    nextN = tempHead.next
                    tempHead.next = prevHead
                    lPointer.next = nextN
                
                if isFirstRun:
                    head = tempHead
                    isFirstRun = False
                else:
                    prevLPointer.next = tempHead

                rPointer = lPointer    
                prevLPointer = lPointer
                lPointer = lPointer.next
                count = 0

        return head

"""
Time complexity = O(n)
Space complexity = O(1)
"""