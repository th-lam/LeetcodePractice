"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1: 
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head

        count = 1
        tail = head

        while tail.next:
            tail = tail.next
            count += 1
        
        k %= count
        if k == 0: return head
        newTailPos = count - k - 1

        tail.next = head
        newTail = head

        while newTailPos > 0:
            newTail = newTail.next
            newTailPos -= 1
        
        newHead = newTail.next
        newTail.next = None
        return newHead

"""
Time complexity = O(n)
Space complexity = O(1)
"""