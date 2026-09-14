# 83. Remove Duplicates from Sorted List

> **Difficulty:** Easy  

> **Tags:** Linked List

> **LeetCode Link:** [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Use two pointers to traverse the list. One pointer marks the last unique node, and the other scans ahead. When a duplicate is found, skip it.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each node is visited once |
| **Space** | O(1) | Only a constant number of pointers are used. |