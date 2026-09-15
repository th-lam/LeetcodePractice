 # 92. Reverse Linked List II
> **Difficulty:** Medium  

> **Tags:** Linked List

> **LeetCode Link:** [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Find the node before the section to reverse. Then repeatedly take the next node from the unreversed part and insert it at the front of the reversed section. 

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | In the worst case, each element is visited once. |
| **Space** | O(1) | Only a constant number of pointers are used. |