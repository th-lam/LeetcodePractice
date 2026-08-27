# 47. Permutations II

> **Difficulty:** Medium  

> **Tags:** Array, Backtracking

> **LeetCode Link:** [47. Permutations II](https://leetcode.com/problems/permutations-ii/solutions/8485146/permutations-ii-by-ehgrd-whib)

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

The approach is similar to 46. Permutations. However, we need to skip a number if it is the same as its predecessor and that predecessor has not been used in the current branch.

## Approach

1. **Backtracking:**
    - The detailed approach of backtracking can refer to 46. Permutations

2. **Preparation:**
    - Sort `nums` so that duplicates are grouped together so that we can check whether a number's predecessor share the same value with it.

3. **Pruning rule:**
    - If `nums[i] == nums[i-1]` and `used[i-1]` is false, skip `nums[i]`.
    
    > Example: `nums` = [1,2,1] -> sorting -> [1,1,2]

    > **Recursion 1**: [1] (`nums[0]`) -> backtracking and generate res[[1,1,2], [1,2,1]] -> mark 1 as unused (both 1,1,2 are unused now) -> [] -> continue to loop

    > **Recursion 1**: [] -> (`nums[1]`) share the same value with its predecessor and its predecessor is unused -> continue -> [2] -> backtrack()

    > **Recursion 2**: [2] -> 1 (`nums[0]`) is not used -> [2,1] -> backtrack()

    > **Recursion 3**: [2] -> since `nums[0]` is used and 1 (`nums[1]`) is not used -> [2,1,1] -> backtrack()
    
## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n! × n) | There are n! permutations in the worst case. Recording each valid permutation requires copying a list of length n. Sorting adds O(n log n), which is dominated by the backtracking. |
| **Space** | O(n) | The recursion depth is at most n. The `path` and `used` arrays each consume O(n) auxiliary space. |        