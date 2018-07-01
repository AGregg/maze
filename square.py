class Square:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
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

    def distance_to_square(self, square):
        return abs(square.x - self.x) + abs(square.y - self.y)

    def adjacent_squares(self, maze):
        adjacent_squares = set()
        if maze[self.x + 1][self.y] == "_":
            adjacent_squares.add(Square(self.x + 1, self.y, self))
        if maze[self.x - 1][self.y] == "_":
            adjacent_squares.add(Square(self.x - 1, self.y, self))
        if maze[self.x][self.y + 1] == "_":
            adjacent_squares.add(Square(self.x, self.y + 1, self))
        if maze[self.x][self.y - 1] == "_":
            adjacent_squares.add(Square(self.x, self.y - 1, self))
        return adjacent_squares
