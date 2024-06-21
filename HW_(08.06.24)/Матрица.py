# __matmul__ - __matmul__(self, other) — умножение матриц, оператор @
# __mul__ - __mul__(self, other) — умножение, оператор *

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dtype = type(matrix[0][0])

    def __mul__(self, other):

        length = len(self.matrix)
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result_matrix

    def __matmul__(self, other):

        m = len(self.matrix)  # a: m × n
        n = len(other.matrix)  # d: n × k
        k = len(other.matrix[0])

        result = [[None for __ in range(k)] for __ in range(m)]  # c: m × k

        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.matrix[i][kk] * other.matrix[kk][j] for kk in range(n))

        return result

    # def count(self, other):
    #
    #     m = len(self.matrix)  # a: m × n
    #     n = len(other.matrix)  # d: n × k
    #     k = len(other.matrix[0])
    #
    #     result = [[None for __ in range(k)] for __ in range(m)]  # c: m × k
    #
    #     for i in range(m):
    #         for j in range(k):
    #             result[i][j] = sum(self.matrix[i][kk] * other.matrix[kk][j] for kk in range(n))
    #
    #     return result

    def __str__(self):
        result = '['
        for line in self.matrix:
            result += '[' + ' '.join([str(elem) for elem in line]) + ']\n'
        return result[:-1] + ']'


a = Matrix([[1, 2],
            [3, 4]])
b = Matrix([[5, 6],
            [7, 8]])
c = Matrix([[1, 2, 3],
            [4, 5, 6]])

print(a * b)
print(a @ c)
# print(a.count(c))


