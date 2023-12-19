input = open("Day 18/input.txt", "r").read().split("\n")
from enum import Enum
class Direction(Enum):
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)
lagoon = [["."]]
corners = []

def expand_lagoon(lagoon, amount = 1, direction = Direction.R):
    if direction == Direction.R:
        for line in lagoon:
            for i in range(amount):
                line.append(".")
    elif direction == Direction.L:
        for line in lagoon:
            for i in range(amount):
                line.insert(0, ".")
        for pos in corners:
            pos[0] += 1


def append_lagoon(lagoon, amount = 1, direction = Direction.D):
    if direction == Direction.D:
        for i in range(amount):
            lagoon.append(["."]*len(lagoon[0]))
    elif direction == Direction.U:
        for i in range(amount):
            lagoon.insert(0, ["."]*len(lagoon[0]))
        for pos in corners:
            pos[1] += 1


current_pos = (0, 0)
floodFill_tests = []
for y, line in enumerate(input):
    
    line_split = line.split()
    direction, amount, color = line_split[0], int(line_split[1]), line_split[2]
    for x in range(amount):
        edge = "#"
        if  x == amount - 1:
            edge = "%"
        if direction == Direction.U.name:
                current_pos = (current_pos[0], current_pos[1] - 1)
                if current_pos[1] < 0:
                    append_lagoon(lagoon, 1, Direction.U)
                    current_pos = (current_pos[0], current_pos[1] + 1)
                lagoon[current_pos[1]][current_pos[0]] = edge
                #if lagoon[current_pos[1]][current_pos[0]+1] == ".":
                #   lagoon[current_pos[1]][current_pos[0]+1] = "1"
                #floodFill_tests.append([current_pos[0], current_pos[1] + 1])
        
        elif direction == Direction.D.name:
                current_pos = (current_pos[0], current_pos[1] + 1)
                if current_pos[1] >= len(lagoon):
                    append_lagoon(lagoon, 1, Direction.D)
                lagoon[current_pos[1]][current_pos[0]] = edge
        
        elif direction == Direction.L.name:
                current_pos = (current_pos[0] - 1, current_pos[1])
                if current_pos[0] < 0:
                    expand_lagoon(lagoon, 1, Direction.L)
                    current_pos = (current_pos[0] + 1, current_pos[1])
                lagoon[current_pos[1]][current_pos[0]] = edge
        
        elif direction == Direction.R.name:
                current_pos = (current_pos[0] + 1, current_pos[1])
                if current_pos[0] >= len(lagoon[0]):
                    expand_lagoon(lagoon, 1, Direction.R)
                lagoon[current_pos[1]][current_pos[0]] = edge
        if  x == amount - 1:
            corners.append([current_pos[0], current_pos[1]])
#Now lagoon is drawn, now floodfill to find amount of lava
'''
for y, line in enumerate(lagoon):
    for x, char in enumerate(line):
        if char == "%":
            print(x, y)'''
sum_edge = 0
for line in lagoon:
    sum_edge += line.count("#")
    print("".join(line))
coords = [[0,6],[0,0],[2,0],[2,2],[5,2],[5,0],[7,0],[7,1],[9,1],[9,6],[7,6],[7,4],[5,4],[5,6]]
#Shoelace formula
area = 0
coords = corners
for i in range(len(coords)):
    if i == len(coords) - 1:
        area += coords[i][0] * coords[0][1] - coords[0][0] * coords[i][1]
    else:
        area += coords[i][0] * coords[i+1][1] - coords[i+1][0] * coords[i][1]
area = abs(area) / 2 + (sum_edge+len(coords))/2 + 1
print(area)
