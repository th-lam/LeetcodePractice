"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = dummyHead = ListNode(next=head)
        right = head

        while right:
            if right.next and right.val == right.next.val:
                while right.next and right.val == right.next.val:
                    right = right.next
                left.next = right.next
            else:
                left = left.next
    
            right = right.next

        return dummyHead.next

"""
Time complexity = O(n)
Space complexity = O(1)
"""