# 25. Reverse Nodes in a k-Group

> **Difficulty:** Hard
> **Tags:** Linked List
> **LeetCode Link:** [25. Reverse Nodes in a k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/8483083/reverse-nodes-in-k-group-by-ehgrd-4k73)
> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Separate the list into segment at a time using two pointers. For each segment, reverse it in-place by inserting new head. Then reconnect the reversed segment back into the main list.

## Approach

1. **Initialize:**:
    - Use a `dummyHead` to simplify edge cases, allowing every segment to be processed with identical logic.
    - `left` pointer anchors the last node of the previous segment. After a new segment is reversed, `left` is connected to the new head of the reversed segment. 
    - `right` pointer scans forward to identify complete segments of `k` nodes. Once `right` has moved `k` steps, the segment bounded by `left.next` and `right` is ready for reversal.

2. **Segment Reversal:**
    - `groupTail` anchors the tail of reversed segment (the original first node).
    - `groupPrev` tracks the current head of the reversed segment.
    - In each iteration, the node right after `groupTail` (`groupHead`) is extracted and inserted at the front of `groupPrev`.

3. **Advance & Repeat:** 
    - After reversal, `left` and `right` are both moved to `groupTail` (which is now the last node of the reversed group), and then continue to scan for the next segment.

## Complexity 
|--------|-----------|-------------|
| **Time** | O(n) | Every node is visited at most twice: once by `right` during scanning, and once during the in-group reversal. |
| **Space** | O(1) | Only a fixed number of pointer variables are used. |