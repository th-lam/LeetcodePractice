# 5. Longest Palindromic Substring

> **Difficulty:** Medium  

> **Tags:** String, Two Pointers 

> **LeetCode Link:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/solutions/8485908/longest-palindromic-substring-expand-fro-1ziy)

> **Solution:** [`solution_expand_around_center.py`](./solution_expand_around_center.py)

---

## Intuition

Treat every character (and every pair of adjacent characters) as the center of a potential palindrome, then expand outward from the center in both directions. Record the longest valid palindrome found.

## Approach

1. **Expand around center**
   - For each character in `s`, treat it as a `center` to expand outward continuously when the characters of `left` and `right` are equal.

2. **Check both odd and even length cases**
  - For each index `center` in the `s`:
    - **Odd length:** `expandFromCenter(center, center)`, the center is a single character.
    - **Even length:** `expandFromCenter(center, center + 1)`, the center lies between two characters.

3. **Track the maximum**
  - After each expansion, compare the current palindrome length with `maxLen`.
  - If a longer palindrome is found, update `maxLen` and `maxStart`.

4. **Return**
  - Extract and return the substring from `maxStart` with length `maxLen`.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n ^ 2) | There are `n` centers; each expansion may scan up to `n` characters in the worst case. |
| **Space** | O(1) | Only a constant number of variables are used. |        