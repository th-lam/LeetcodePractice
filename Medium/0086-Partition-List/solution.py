"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerCur = smallerDummy = ListNode(0, None)
        greaterCur = greaterDummy = ListNode(0, None)
        cur = head
        
        while cur:
            if cur.val < x:
                smallerCur.next = cur
                smallerCur = smallerCur.next
            else:
                greaterCur.next = cur
                greaterCur = greaterCur.next
            cur = cur.next

        smallerCur.next = greaterDummy.next
        greaterCur.next = None

        return smallerDummy.next

"""
Time complexity = O(n)
Space complexity = O(1)
"""