 # 61. Rotate List
> **Difficulty:** Medium  

> **Tags:** Linked List

> **LeetCode Link:** [61. Rotate List](https://leetcode.com/problems/rotate-list)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Connect the tail to the head to form a circular list. Find the position of the new tail. Set the next pointer of the new tail to `None` to break the circle.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited at most twice. |
| **Space** | O(1) | Only a constant number of pointers are used. |