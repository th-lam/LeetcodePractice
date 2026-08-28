# 20. Valid Parentheses

> **Difficulty:** Easy  

> **Tags:** Stack

> **LeetCode Link:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Use a stack to store unmatched opening brackets. When encountering a closing bracket, check if it matches the most recent opening bracket on top of the stack. If the stack is empty or the top does not match, the parentheses is invalid.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each character is processed once in the worst case; stack push and pop operations are O(1). |
| **Space** | O(n) | The stack holds at most all opening brackets in the worst case (e.g., `(((((`). |