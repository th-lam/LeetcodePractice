# 69. Sqrt(x)

> **Difficulty:** Easy  

> **Tags:** Binary Search

> **LeetCode Link:** [69. Sqrt(x)](https://leetcode.com/problems/sqrtx)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Use a binary search to find the largest integer whose square is less than or equal to x.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(log n) | The search space is halved in each iteration. |
| **Space** | O(1) | Only a constant number of pointers are used. |