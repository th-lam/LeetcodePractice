# 77. Combinations

> **Difficulty:** Medium  

> **Tags:** Backtracking

> **LeetCode Link:** [47. Permutations II](https://leetcode.com/problems/combinations/solutions/8485236/combinations-by-ehgrd-9u1x)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Find every k-length combination by choosing numbers in ascending order. Use a `start` index to ensure each new number is larger than the previous one (e.g. `[1,3]` and `[3,1]` are the same combination), ensuring the result are combinations instead of permutations. When the remaining numbers are insufficient to form a combination of size `k`, the loop break.

## Approach

1. **Initialize:**
    - `res` stores all completed combinations.
    - `path` records the current sequence of chosen numbers.

2. **Backtrack with a start index**
    - `start` marks the smallest number that will be picked next. This ensure a ascending order and prevents the same combination from being generated in different orders.
    
    > Example: If `start` = 2, the next number chosen will only be > 2, which prevent the combination of [2,1] (as [1,2] have already been found).

3. **Pruning rule:**
    - Check whether the count of remaining numbers (`n - i + 1`) plus the current `path` length can still reach `k`. If `len(path) + (n - i + 1) < k`, break the loop immediately.
    
    > Example: n = 10, k = 3, i = 9, `path` = []
    
    > Remaining numbers = 10 - 9 + 1 = 2 (9 is not yet picked)

    > `len(path)`(0) + 2 < 3. As there remains no combination, break the loop immediately

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(k × C(n, k)) | There are C(n, k) valid k-combinations. Recording each valid combination requires copying a list of length k.
| **Space** | O(k) | The recursion depth is at most k. The `path` consume O(k) auxiliary space. |        