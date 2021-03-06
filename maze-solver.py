from square import *
import heapq

with open("maze.txt") as maze:
    maze_array = [list(line.strip()) for line in maze]

last_row = len(maze_array) - 1
last_column = len(maze_array[0]) - 1

for x in range(len(maze_array[last_row])):
    if (maze_array[last_row][x] == "_"):
        end_square = Square(last_row,x,None)
        break

for x in range(len(maze_array[0])):
    if (maze_array[0][x] == "_"):
        start_square = Square(0,x,None)
        break

second_square = Square(start_square.x + 1, start_square.y, start_square)
count = 0

visited_squares = set([start_square])
frontier = []
heapq.heapify(frontier)
heuristic = second_square.distance_traversed + second_square.distance_to_square(end_square)
heapq.heappush(frontier, (heuristic, 0, second_square))
while len(frontier):
    h, c, current_square = heapq.heappop(frontier)
    visited_squares.add(current_square)
    if current_square == end_square:
        end_square = current_square
        break
    adjacent_squares = current_square.adjacent_squares(maze_array) - visited_squares
    for adjacent_square in adjacent_squares:
        count += 1
        heuristic = adjacent_square.distance_traversed + adjacent_square.distance_to_square(end_square)
        heapq.heappush(frontier, (heuristic, count, adjacent_square))

current = end_square
alphabet = "abcdefghijklmnopqrstuvwxyz"
while current:
    maze_array[current.x][current.y] = alphabet[current.distance_traversed % 26]
    current = current.parent

for line in maze_array:
    print(*line)
