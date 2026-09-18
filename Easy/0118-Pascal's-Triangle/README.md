# 118. Pascal's Triangle

> **Difficulty:** Easy  

> **Tags:** Dynamic Programming

> **LeetCode Link:** [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Build the triangle row by row. Each new row starts and ends with 1. Each number in the between is the sum of the two numbers directly above it in the previous row.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n ^ 2) |  |
| **Space** | O(n ^ 2) |  |