"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = right = dummyHead = ListNode(None, head)

        while right.next is not None:
            right = right.next
            
            if left.val == right.val:
                left.next = right.next
                continue
            
            left = left.next

        return dummyHead.next

"""
Time complexity = O(n)
Space complexity = O(1)
"""