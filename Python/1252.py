class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = [[0 for i in range(m)] for j in range(n)]
        for index in indices:
            for i in range(m):
                res[index[0]][i] += 1
            for i in range(n):
                res[i][index[1]] += 1

        return [res[i][j] % 2 == 1 for i in range(n) for j in range(m)].count(True)