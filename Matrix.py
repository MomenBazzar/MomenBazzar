class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def cell(self, row, col, val):
        self.matrix[row][col] = val

    @classmethod
    def zeroMatrix(cls, rows: int, columns: int):
        if columns < 1:
            columns = 1
        if rows < 1:
            rows = 1
        return cls([[0 for i in range(rows)] for j in range(columns)])

    @classmethod
    def add(cls, m1, m2):
        if len(m1.matrix) != len(m2.matrix) or len(m1.matrix[0]) != len(m2.matrix[0]):
            raise ValueError("can't add matrices with different dimensions.")

        res_matrix = [[0 for i in range(len(m1.matrix[0]))] for j in range(len(m1.matrix))]
        for i in range(len(m1.matrix)):
            for j in range(len(m1.matrix[0])):
                res_matrix[i][j] = m1.matrix[i][j] + m2.matrix[i][j]

        return cls(res_matrix)

    @classmethod
    def sub(cls, m1, m2):
        if len(m1.matrix) != len(m2.matrix) or len(m1.matrix[0]) != len(m2.matrix[0]):
            raise ValueError("can't add matrices with different dimensions.")

        res_matrix = [[0 for i in range(len(m1.matrix[0]))] for j in range(len(m1.matrix))]
        for i in range(len(m1.matrix)):
            for j in range(len(m1.matrix[0])):
                res_matrix[i][j] = m1.matrix[i][j] - m2.matrix[i][j]

        return cls(res_matrix)

    @classmethod
    def scale(cls, self, val=1):
        res_matrix = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res_matrix[i][j] = self.matrix[i][j] * val
        return cls(res_matrix)

    @classmethod
    def transpose(cls, self):
        res_matrix = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res_matrix[j][i] = self.matrix[i][j]
        return cls(res_matrix)

    @classmethod
    def dot(cls, m1, m2):
        if len(m1.matrix[0]) != len(m2.matrix):
            raise ValueError("nonvalid dot product dimensions")

        res_matrix = [[0 for i in range(len(m1.matrix))] for j in range(len(m2.matrix[0]))]
        for i in range(len(m1.matrix)):
            for j in range(len(m2.matrix[0])):
                for k in range(len(m2.matrix)):
                    res_matrix[i][j] += m1.matrix[i][k] * m2.matrix[k][j]
        return cls(res_matrix)

    @classmethod
    def determenent(cls, mx):
        if len(mx.matrix) > 2:
            det = 0
            for x in range(len(mx.matrix[0])):
                before_mx = [[mx.matrix[i][j] for j in range(0, x)] for i in range(1, len(mx.matrix))]
                after_mx = [[mx.matrix[i][j] for j in range(x + 1, len(mx.matrix[0]))] for i in
                            range(1, len(mx.matrix))]
                for i in range(len(before_mx)):
                    for j in range(len(after_mx[i])):
                        before_mx[i].append(after_mx[i][j])
                det += ((-1) ** x) * mx.matrix[0][x] * mx.determenent(cls(before_mx))
            return det

        if len(mx.matrix) == 2:
            res = (mx.matrix[0][0] * mx.matrix[1][1]) - (mx.matrix[0][1] * mx.matrix[1][0])
            return res


# tester1 = Matrix.zeroMatrix(2, 3)
# tester1.cell(1, 1, 11)
# tester1.cell(2, 0, 3)
# tester2 = Matrix([[3, 6],
#                   [5, 1],
#                   [8, 7]])
# print(tester1.matrix)
# print(tester2.matrix)
# result = Matrix.add(tester1, tester2)
# print(f"result of addition = {result.matrix}")
# result = Matrix.sub(tester2, tester1)
# print(f"result of subtraction = {result.matrix}")
# tester2.scale(2)
# print(f"tester2 scaled by 2 is {tester2.matrix}")
# tester2.transpose()
# print(f"tester2 after transpose is {tester2.matrix}")
# a = Matrix([
#             [2, 5, 0, 3],
#             [-1, 2, 3, -2],
#             [2, 1, -2, 0],
#             [2, 1, 4, 7]
#             ])
# b = Matrix([[2, 1, 2],
#             [3, 2, 4]])
# res = Matrix.dot(a, b)
# print(f"res of dot product = {res.matrix}")
# print(Matrix.determenent(a))
