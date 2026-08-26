"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

"""
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        curN = dummyHead = ListNode(next=head)

        while curN.next is not None:
            curN = curN.next
            if curN.val in seen:
                seen[curN.val] = "skip"
            else:
                seen[curN.val] = curN

        dummyHead.next = None
        curN = dummyHead
        for key in seen:
            if seen[key] != "skip":
                curN.next = seen[key]
                curN = curN.next
                curN.next = None

        return dummyHead.next

"""
Time complexity = O(n)
Space complexity = O(n)
"""