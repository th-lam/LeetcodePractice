# 26. Remove Duplicates from Sorted Array

> **Difficulty:** Easy  

> **Tags:** Two Pointers, Array

> **LeetCode Link:** [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Since the array is sorted, all duplicate values appear consecutively. Use a slow pointer to mark the last unique element and a fast pointer to scan for the next element. When a new unique element is found, move the slow pointer forward and overwrite that position with the new element .

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited once. |
| **Space** | O(1) | Only a constant number of pointers are used. |