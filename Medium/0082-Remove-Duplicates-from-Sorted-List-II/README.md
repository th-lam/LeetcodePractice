# 82. Remove Duplicates from Sorted List II

> **Difficulty:** Medium  

> **Tags:** Linked List  

> **LeetCode Link:** [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solutions/8483626/remove-duplications-from-sorted-list-ii-jhctm)

> **Solution:** [`solution_optimized.py`](./solution_optimized.py)

---

## Intuition

Traverse the sorted list once, identifying consecutive duplicate values and skipping them entirely. A `right` pointer moves forward to find the consecutive duplicate values, while a `left` pointer join the unique nodes into the final list.

## Approach

1. **Initialize:**
    - Use a `dummyHead` to handle edge cases where duplicates occur at start.
    - `left` pointer anchors to the last confirmed unique node and only moves forward when it confirm that "right" points to a unique node.
    - `right` pointer scans forward to identify duplicated elements.

2. **Scan for duplicates:**
    - If `right` is  followed by a duplicate, it will move forward until it reaches the final node of that value. Then set `left.next = right.next` to skip all the duplicated nodes.
    - If `right` is not followed by a duplicate, move `left` forward by one step.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each node is visited at most once by `right`. |
| **Space** | O(1) | Only a fixed number of pointer variables are used. |

## Alternative
> **Tags:** Linked List, Hash Table  
> **Solution:** [`solution_alternative.py`](./solution_alternative.py)

 Traverse the list once to identify which values are unique and which appear multiple times. Use a dictionary to store the first node encountered for each value. If the value appears again, we mark it for complete removal. Reconstruct the result list by linking only the nodes whose values are marked as unique.

 This approach require O(n) space but it can work from unsorted list.