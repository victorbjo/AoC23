input = open("Day 18/input.txt", "r").read().split("\n")
from enum import Enum
class Direction(Enum):
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)
color2dir = {3: Direction.U, 1: Direction.D, 2: Direction.L, 0: Direction.R}
lagoon = [["."]]
corners = []
size_lagoon =[1,1]
def expand_lagoon(lagoon, amount = 1, direction = Direction.R):
    if direction == Direction.R:
        size_lagoon[0] += amount
    elif direction == Direction.L:
        size_lagoon[0] += amount
        for pos in corners:
            pos[0] += 1


def append_lagoon(lagoon, amount = 1, direction = Direction.D):
    if direction == Direction.D:
        size_lagoon[1] += amount
    elif direction == Direction.U:
        size_lagoon[1] += amount
        for pos in corners:
            pos[1] += 1


current_pos = [0, 0]
floodFill_tests = []
sum_edge = 0

for y, line in enumerate(input):    
    line_split = line.split()
    direction, amount, color = line_split[0], int(line_split[1]), line_split[2]
    direction = color2dir[int(color[-2:-1])].name
    amount_color = color[2:-2]
    amount = int(amount_color, 16)
    #print(amount_color, direction_color)
    #for x in range(amount):
    sum_edge += amount
    #old_pos = current_pos.copy()
    if direction == Direction.U.name:
            corners.append([current_pos[0], current_pos[1]])
            current_pos = (current_pos[0], current_pos[1] - amount)
            if current_pos[1] < 0:
                append_lagoon(lagoon, 1, Direction.U)
                current_pos = (current_pos[0], current_pos[1] + 1)
    
    elif direction == Direction.D.name:
            corners.append([current_pos[0], current_pos[1]])
            current_pos = (current_pos[0], current_pos[1] + amount)
            if current_pos[1] >= size_lagoon[1]:
                append_lagoon(lagoon, 1, Direction.D)
            #lagoon[current_pos[1]][current_pos[0]] = edge
    
    elif direction == Direction.L.name:
            corners.append([current_pos[0] , current_pos[1]])
            current_pos = (current_pos[0] - amount, current_pos[1])
            if current_pos[0] < 0:
                expand_lagoon(lagoon, 1, Direction.L)
                current_pos = (current_pos[0] + 1, current_pos[1])
            #lagoon[current_pos[1]][current_pos[0]] = edge
    
    elif direction == Direction.R.name:
            corners.append([current_pos[0], current_pos[1]])
            current_pos = (current_pos[0] + amount, current_pos[1])
            if current_pos[0] >= size_lagoon[0]:
                expand_lagoon(lagoon, 1, Direction.R)
            #lagoon[current_pos[1]][current_pos[0]] = edge
    #if  x == amount - 1:
    
#Now lagoon is drawn, now floodfill to find amount of lava
'''
for y, line in enumerate(lagoon):
    for x, char in enumerate(line):
        if char == "%":
            print(x, y)'''
#sum_edge = 0
print(sum_edge)
coords = [[0,6],[0,0],[2,0],[2,2],[5,2],[5,0],[7,0],[7,1],[9,1],[9,6],[7,6],[7,4],[5,4],[5,6]]
#Shoelace formula
area = 0
coords = corners
for i in range(len(coords)):
    if i == len(coords) - 1:
        area += coords[i][0] * coords[0][1] - coords[0][0] * coords[i][1]
    else:
        area += coords[i][0] * coords[i+1][1] - coords[i+1][0] * coords[i][1]
area = abs(area) / 2 + (sum_edge)/2 + 1
print(area)
#print(sum_edge)
#print(len(corners), "Corners")

#for x, corner in enumerate(corners):
    #print(corner)
    #if [corner[1], corner[0]] in coords:
        #print(x)