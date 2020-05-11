class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        
        for each in matrix_string.split("\n"):
            rows = []
            one = each.split(" ")
            for num in one:
                rows.append(int(num))
            self.matrix.append(rows)
            rows = []

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [each[index-1] for each in self.matrix]


if __name__ == "__main__":
    str_matrix = "9 8 7\n51 3 2\n6 6 7"

    matrix = Matrix(str_matrix)
    print(matrix.row(1))
    print(matrix.column(2))