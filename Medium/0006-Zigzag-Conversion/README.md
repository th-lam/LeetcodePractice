# 6. Zigzag Conversion

> **Difficulty:** Medium  

> **Tags:** String

> **LeetCode Link:** [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Distribute the characters into different list according to their row by moving downward from the top row to the bottom row, then upward back to the top. Once all characters are distributed, join the lists to form the final string.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each characters is visited once. |
| **Space** | O(n) | All characters are stored once. |