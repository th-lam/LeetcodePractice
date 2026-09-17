# 66. Plus One

> **Difficulty:** Easy  

> **Tags:** Array

> **LeetCode Link:** [66. Plus One](https://leetcode.com/problems/plus-one)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Start from the last digit and add one. If the digit is 9, it becomes 0 and the carry moves to the next digit. If the digit is less than 9, simply plus one and return immediately. If every digit is 9, insert 1 at the front.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | In the worst case, all digits are 9 and each digit is visited once. |
| **Space** | O(1) | The list is modified in-place. |