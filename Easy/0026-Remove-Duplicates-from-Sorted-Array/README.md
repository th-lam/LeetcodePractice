# 26. Remove Duplicates from Sorted Array

> **Difficulty:** Easy  

> **Tags:** Two Pointers, Array

> **LeetCode Link:** [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Since the array is sorted, all duplicate values appear consecutively. We can determine whether a value is unique by comparing it with its previous element. Use a slow pointer to mark the last unique element and a fast pointer to scan through the array. When the value of the element marked by the fast pointer is different with the value of the element marked by the slow pointer, a new unique element is found. Then, move the slow pointer forward and overwrite that position with the new unique element .

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited once. |
| **Space** | O(1) | Only a constant number of pointers are used. |