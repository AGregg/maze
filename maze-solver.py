from square import *

with open("maze.txt") as maze:
    maze_array = [list(line.strip()) for line in maze]

for x in range(len(maze_array[0])):
    if (maze_array[0][x] == "_"):
        start_square = Square(0,x)
        break

last_row = len(maze_array) - 1
for x in range(len(maze_array[last_row])):
    if (maze_array[last_row][x] == "_"):
        end_square = Square(last_row,x)
        break

print(maze_array)
print(start_square.x)
print(start_square.y)
print(end_square.x)
print(end_square.y)
