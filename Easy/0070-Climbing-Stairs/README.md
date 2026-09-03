# 70. Climbing Stairs

> **Difficulty:** Easy  

> **Tags:** Binary Search

> **LeetCode Link:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Step `n` can come from either step `n-1` (moving 1 step) or step `n-2` (moving 2 step). Therefore, the number of ways to reach step `n` follows a fibonacci sequence ( `f(n) = f(n-1) + f(n-2)` ).

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | A single loop iterate from 3 to n |
| **Space** | O(1) | Only a constant number of variables are used. |