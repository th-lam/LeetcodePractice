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

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        dummyHead = ListNode(next=head)
        left = right = dummyHead
        count = 0

        while right.next is not None:
            right = right.next
            count += 1

            if count == k:
                groupPrev = groupTail = left.next
                
                for _ in range(k-1):
                    groupHead = groupTail.next
                    groupNext = groupHead.next
                    groupHead.next, groupTail.next = groupPrev, groupNext
                    groupPrev = groupHead

                left.next = groupPrev
                left = right = groupTail
                count = 0
        
        return dummyHead.next


"""
Time complexity = O(n)
Space complexity = O(1)
"""