# 1. Two Sum

> **Difficulty:** Easy  

> **Tags:** Hash Table

> **LeetCode Link:** [1. Two Sum](https://leetcode.com/problems/two-sum)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Traverse the array once while storing the complement of each number in a hash map. If the current number has already been stored as a compliment by a previous element, return the indices.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each number is visited once in the worst case. Hashmap operations are O(1) on average. |
| **Space** | O(n) | The hashmap stores n elements in the worst case. |