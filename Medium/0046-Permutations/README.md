# 46. Permutations

> **Difficulty:** Medium  

> **Tags:** Array, Backtracking

> **LeetCode Link:** 

> **Solution:** [`solution.py`](./solution.py)

---

## Intuition

Find out every possible order with backtracking. At each level of recursion, choose an unused number from `nums`, append it to the current path. When the path reaches the same length as `nums`, a complete permutation is found. Then, backtrack by popping the last element in `path` to try another unused number at the same position.

## Approach

1. **Initialize:**
   - `res` stores all completed permutations.
   - `path` records the current sequence of chosen numbers.
   - `used` is a boolean array used for checking which indices in `nums` have already been used.

2. **Backtrack**
   - **Base case:** 
        - If `len(path) == len(nums)`, the current path is a valid permutation. Append a shallow copy (`path[:]`) to `res` and return.
   > If `res.append(path)`, res will store the reference of `path`, which will be changed when we modifying it in the following recursion.

    - **Recursive case:** 
        - Loop through every index `i` in `nums`.
        - If `used[i]` is `True`, skip it to avoid duplicates.
        - Otherwise, mark `used[i] = True`, append `nums[i]` to `path`, and recursively call `backtrack()` to fill the next position.
        - **Undo:** After the recursive call returns, set `used[i] = False` and `pop()` from `path`. This restores the state so the parent level can try the next candidate.
    
    > Example: num = [1,2,3]

    > **Recursion 1**: [1] -> backtrack()

    > **Recursion 2**: 1 is used -> [1, 2] -> backtrack()

    > **Recursion 3**: 1 and 2 are used -> [1, 2, 3] -> backtrack()


    > **Recursion 4**: Base case -> return

    > **Return Recursion 3**: -> set 3 to be unused -> [1, 2] -> Loop is finished -> return

    > **Return Recursion 2**: -> set 2 to be unused -> [1] -> continue loop -> [1, 3] -> backtrack()

    > **Recursion 3**: 1 is used -> [1, 3, 2] -> backtrack()

## Complexity 
|   | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n! × n) | There are n! permutations in total. Recording each valid permutation requires copying a list of length n. |
| **Space** | O(n) | The recursion depth is at most n. The `path` and `used` arrays each consume O(n) auxiliary space. |
