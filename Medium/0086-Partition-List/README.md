 # 86. Partition List
> **Difficulty:** Medium  

> **Tags:** Linked List

> **LeetCode Link:** [86. Partition List](https://leetcode.com/problems/partition-list)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Split the list into two separate list (values smaller than `x`, and values greater than or equal to `x`). Then, connect the smaller list in front of the larger list.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited once. |
| **Space** | O(1) | Only a constant number of pointers are used. |