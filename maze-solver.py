with open("maze.txt") as maze:
    maze_array = [list(line.strip()) for line in maze]

print(maze_array)
