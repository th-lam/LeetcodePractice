# 18. 4Sum

> **Difficulty:** Medium  

> **Tags:** Two Pointers

> **LeetCode Link:** [18. 4Sum](https://leetcode.com/problems/4sum)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Sort the array and fix two numbers with nested loops to reduce the problem to a **2Sum** problem. Use two pointers on the remaining range to find pairs that complete the sum to target. Skip the duplicate values to avoid repeated quadruplets.

## Approach
1. **Sort**
   - Sort `nums` to enable the two-pointer scan, pruning, and duplicate skipping.

2. **Fix the first number**
   - Loop `i` over `range(len(nums) - 3)`.
   - If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicate quadruplets.
   - Compute the smallest possible sum for this fixed `i`. If it already exceeds `target`, break the outer loop because all larger `i` will only increase the sum.

3. **Fix the second number**
   - Loop `j` over `range(i + 1, len(nums) - 2)`.
   - If `j > i + 1` and `nums[j] == nums[j-1]`, skip to avoid duplicate quadruplets.
   - Compute the smallest possible sum for this pair `(i, j)`. If it exceeds `target`, break the inner loop.
   - Compute the greatest possible sum for this pair `(i, j)`. If it is still below `target`, continue to the next `j`.

4. **Two-pointer scan**
    - Set `left = j + 1` and `right = len(nums) - 1`.
    - While `left < right`:
        - Compute the sum of `nums[i]`, `nums[j]`, `nums[left]` and `nums[right]`
        - If the sum  is less than `target`, move `left` rightward.
        - If the sum is greater, move `right` leftward.
        - If the sum equals `target`, record the quadruplets.

5. **Skip duplicates**
   - After finding a valid quadruplets, use a while loop to move `left` and `right` past the duplicate values.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n ^ 3) | The two outer loop runs O(n ^ 2) times. The inner two-pointer scan runs O(n) for each fixed pair. Sorting costs O(n log n), which is dominated by O(n ^ 3). |
| **Space** | O(1) | Only a fixed amount of extra space is used for the pointers. This excludes the output space required to store all quadruplets.|