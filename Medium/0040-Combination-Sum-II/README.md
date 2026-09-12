# 40. Combination Sum II

> **Difficulty:** Medium  

> **Tags:** Backtracking

> **LeetCode Link:** [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Sort the candidates so duplicates become adjacent. Find every combinations via backtracking. Skip duplicate values at the same recursion level to avoid repeated combinations.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(2 ^ n) | In the worst case, the recursion explores all subsets of the candidates. Each candidate is either included or excluded. |
| **Space** | O(n) | The recursion depth is at most n, and the `path` holds at most n elements. This excludes the output space required to store all valid combinations. |