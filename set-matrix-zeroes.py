class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [0 in x for x in matrix]
        cols = [0 in x for x in zip(*matrix)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] *= rows[i]+cols[j] == 0
