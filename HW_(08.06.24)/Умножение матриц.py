# 1
x = [[1, 2],
     [3, 4],
     [5, 6]]
y = [[5, 6],
     [7, 8],
     [9, 10]]

result = []
for i in range(len(x)):
    result.append([0] * len(x[i]))
    for j in range(len(x[i])):
        result[i][j] = x[i][j] * y[i][j]

print(result)

# 2


def f(row, col):
    return sum(elem1 * elem2 for elem1, elem2 in zip(row, col))


x = [[1, 2],
     [3, 4],
     [5, 6]]
y = [[5, 6, 7],
     [8, 9, 10]]

result = []
for i1 in range(len(x)):
    row_x = x[i1]
    result.append([0] * len(y[0]))
    for j2 in range(len(y[0])):
        col_y = []
        for i2 in range(len(y)):
            col_y.append(y[i2][j2])
        result[i1][j2] = f(row_x, col_y)
    print(result[i1])


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.dtype = type(matrix[0][0])

    def __mul__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([0] * len(self.matrix[i]))
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] * other.matrix[i][j]
        return result

    @staticmethod
    def __f(row, col):
        return sum(elem1 * elem2 for elem1, elem2 in zip(row, col))

    def __matmul__(self, other):
        result = []
        for i1 in range(len(self.matrix)):
            row_self = self.matrix[i1]
            result.append([0] * len(other.matrix[0]))
            for j2 in range(len(other.matrix[0])):
                col_other = []
                for i2 in range(len(other.matrix)):
                    col_other.append(other.matrix[i2][j2])
                result[i1][j2] = f(row_self, col_other)
        return result


x = Matrix([[1, 2],
            [3, 4],
            [5, 6]])

y = Matrix([[5, 6],
            [7, 8],
            [9, 10]])

z = Matrix([[5, 6, 7],
            [8, 9, 10]])

print(x * y)
print(x @ z)
