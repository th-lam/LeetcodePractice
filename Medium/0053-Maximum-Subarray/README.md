# 53. Maximum Subarray

> **Difficulty:** Medium  

> **Tags:** Hash Table

> **LeetCode Link:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Keep calculating the sum of the current subarray. For each number, decide whether to expand the current subarray or start over from that number. Record the maximum sum that occurs across all subarrays.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visied once. |
| **Space** | O(1) | Only a constant number of variables are used. |