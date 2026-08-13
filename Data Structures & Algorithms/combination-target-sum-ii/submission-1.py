class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        the difference between this and Combination Sum is we cannot use
        each number more than once

        however any number can appear more than once, and we would be able to
        use that number more than once


        """
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target and curr not in res:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:

                return 

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: # this skips duplicates, significantly reducing our recursion stack
                i += 1
            dfs(i + 1, curr, total)


        dfs(0, [], 0)
        return res