# 16. 3Sum Closest

> **Difficulty:** Medium  

> **Tags:** Two Pointers

> **LeetCode Link:** [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Sort the array and fix one number. Use two pointers on the remaining range to find a pair of numbers such that the total sum of the fixed number and the pair is as close as possible to the target. 

## Approach
1. **Sort**
    - Sort `nums` to enable pruning and two-pointer scan.

2. **Fix the first number**
    - Loop `i` over `range(len(nums) - 2)`.
    - If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid redundant work.

3. **Pruning rule**
    - Compute the smallest possible sum for this fixed `i` (`curMin = nums[i] + nums[i+1] + nums[i+2]`). If `curMin > target`, all sums with larger `i` will only be greater (because the array is sorted). Update `closest` if `curMin` is closer, then break the outer loop.
    - Compute the largest possible sum for this fixed `i` (`curMax = nums[i] + nums[-1] + nums[-2]`) . If `curMax < target`, all sums with this `i` will only be smaller. Update `closest` if `curMax` is closer, then continue to the next `i`.

4. **Two-pointer scan**
    - Set `left = i + 1` and `right = len(nums) - 1`.
    - While `left < right`:
        - Compute the sum of `nums[i]`, `nums[left]` and `nums[right]` and its absolute difference from `target`.
        - If the current difference is smaller than `minDifference`, update `closest` and `minDifference`.
        - If the sum equals `target`, return the sum.
        - If the sum is less than the target, move `left` rightward.
        - If the sum is greater, move `right` leftward.

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n ^ 2) | The outer loop runs O(n) times. The inner two-pointer scan runs O(n) for each fixed `i`. Sorting costs O(n log n), which is dominated by O(n ^ 2). |
| **Space** | O(1) | Only a fixed amount of extra space is used for the pointers and the variables.|