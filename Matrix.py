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
            raise ValueError("can't subtract matrices with different dimensions.")

        res_matrix = [[0 for i in range(len(m1.matrix[0]))] for j in range(len(m1.matrix))]
        for i in range(len(m1.matrix)):
            for j in range(len(m1.matrix[0])):
                res_matrix[i][j] = m1.matrix[i][j] - m2.matrix[i][j]

        return cls(res_matrix)

    def scale(self, val=1):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] * val

    def transpose(self):
        res_matrix = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res_matrix[j][i] = self.matrix[i][j]
        self.matrix = res_matrix

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
# a = Matrix([[2, 2],
#             [0, 3],
#             [0, 4]])
# b = Matrix([[2, 1, 2],
#             [3, 2, 4]])
# res = Matrix.dot(a, b)
# print(f"res of dot product = {res.matrix}")
