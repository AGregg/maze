class Square:
    def __init__(self, x, y, parent, end_square):
        self.x = x
        self.y = y
        self.parent = parent
        if end_square:
            self.end_square = end_square
            self.distance_to_end = self.distance(end_square)
        if parent:
            self.distance_traversed = parent.distance_traversed + 1
        else:
            self.distance_traversed = 0

    def __key(self):
        return (self.x, self.y)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())

    def distance(self, square):
        return abs(square.x - self.x) + abs(square.y - self.y)

    def heuristic(self):
        return self.distance_traversed + self.distance_to_end

    def adjacent_squares(self, maze):
        adjacent_squares = set()
        if maze[self.x + 1][self.y] == "_":
            adjacent_squares.add(Square(self.x + 1, self.y, self, self.end_square))
        if maze[self.x - 1][self.y] == "_":
            adjacent_squares.add(Square(self.x - 1, self.y, self, self.end_square))
        if maze[self.x][self.y + 1] == "_":
            adjacent_squares.add(Square(self.x, self.y + 1, self, self.end_square))
        if maze[self.x][self.y - 1] == "_":
            adjacent_squares.add(Square(self.x, self.y - 1, self, self.end_square))
        return adjacent_squares
