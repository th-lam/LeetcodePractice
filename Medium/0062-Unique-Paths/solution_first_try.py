class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [0]

        def backtrack(curM, curN):
            if curM == m and curN == n:
                res[0] += 1
                return
            elif curM > m: return
            elif curN > n: return


            for i in range(2):
                if i == 0:
                    backtrack(curM + 1, curN)
                if i == 1:
                    backtrack(curM, curN + 1)

        backtrack(1, 1)

        return res[0]