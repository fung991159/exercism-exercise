class Matrix:
    def __init__(self, matrix_string):
        # split string to list and turn string element into integer
        self.m = [list(map(int, row.split())) for row in matrix_string.split('\n')]

    def row(self, index):
        # index base 1
        return self.m[index-1]

    def column(self, index):
        return [row[index-1] for row in self.m]

if __name__ == '__main__':
    in_str = """9 8 7
5 3 2
6 6 7"""
    m = Matrix(in_str)
    print(m.row(3))
