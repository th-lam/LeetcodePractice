 # 27. Remove Element
> **Difficulty:** Easy  

> **Tags:** Two Pointers, Array

> **LeetCode Link:** [26. Remove Element](https://leetcode.com/problems/remove-element)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Use a slow pointer to mark the position for the next valid element and a fast pointer to scan through the array. When the fast pointer encounters an element not equal to `val`, copy that element to the slow pointer's position and advance the slow pointer. 

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited once. |
| **Space** | O(1) | Only a constant number of pointers are used. |