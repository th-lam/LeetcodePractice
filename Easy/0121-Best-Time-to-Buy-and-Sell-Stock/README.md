 # 121. Best Time to Buy and Sell Stock

> **Difficulty:** Easy  

> **Tags:** Array

> **LeetCode Link:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Track the lowest price seen so far while scanning through the list. Find the current highest profits can made by selling at the current price after buying at the lowest price. Keep the highest profit found.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Each element is visited once |
| **Space** | O(1) | Only a constant number of variables are used. |