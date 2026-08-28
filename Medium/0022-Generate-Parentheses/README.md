# 22. Generate Parentheses

> **Difficulty:** Medium  

> **Tags:** Backtracking

> **LeetCode Link:** [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Find every valid combination by adding one parenthesis at a time.  Add a open parenthesis only if it would not exceed the number of `n`. Add a right parenthesis only if it would not exceed the number of left parentheses already placed. This ensure every partial path is valid so the final result needs no filtering.

## Approach
1. **Recursive Tree**
   - ![Generate Parentheses Recursive Tree]((../../assets/0022-Generate-Parentheses/generate_parentheses_recursive_tree.png))

2. **Add open parenthesis first:**
   - If `openCount < n`, append `(` and recurse with `openCount + 1`.

3. **Add close parenthesis:**
   - If `closeCount < openCount`, append `)` and recurse with `closeCount + 1`.
   - This ensures the parentheses remain balanced at every step so that a close parenthesis will never be placed before a open parenthesis.

4. **Base case:**
   - When `len(path) == 2 * n`, a valid combination is completed. Append it to the result and return.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(4^n / √n) | The number of valid parentheses sequences is the n-th Catalan number (1, 2, 5, 14, 42, 132, 429, 1430, 4862), which grows as ~4^n / (n^(3/2) √π). Each valid sequence requires O(n) time to build. Time complexity = 4^n / (n^(3/2) √π) × n ~ 4^n / √n (√π is a linear factor dominated by n^(3/2))|
| **Space** | O(n) | The recursion depth is at most 2n, and the `path` string holds at most 2n characters. This excludes the output space required to store all valid combinations. |