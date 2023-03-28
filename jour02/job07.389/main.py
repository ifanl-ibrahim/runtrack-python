class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for x in range(j)] for y in range(i)]

