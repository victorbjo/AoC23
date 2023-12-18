from enum import Enum
input = open("Day 16/input.txt", "r").read().split("\n")
input = [list(x) for x in input]
import copy
import visualizer
from visualizer import directions
#input_copy = open("Day 16/input.txt", "r").read().split("\n")
#input_copy = [list(x) for x in input]
'''class directions(Enum):
    up = (-1,0)
    down = (1,0)
    left = (0,-1)
    right = (0,1)'''
class Beam:
    def __init__(self, coords, direction):
        self.coords = coords
        self.direction = direction
    def move(self):
        self.coords = (self.coords[0] + self.direction.value[0], self.coords[1] + self.direction.value[1])
    def __repr__(self) -> str:
        return f"Beam({self.coords}, Going {self.direction.name})"
    

def handle_splitter(char, beam, beam_list, visited):
    if char == "|":
        if beam.direction == directions.up or beam.direction == directions.down:
            return
        else:
            visited[beam.coords[0]][beam.coords[1]].append(beam.direction)
            beam.direction = directions.up
            beam_list.append(Beam(beam.coords, directions.down))
    elif char == "-":
        if beam.direction == directions.left or beam.direction == directions.right:
            return
        else:
            visited[beam.coords[0]][beam.coords[1]].append(beam.direction)
            beam.direction = directions.left
            beam_list.append(Beam(beam.coords, directions.right))


special = {"/":{directions.up:directions.right, directions.down:directions.left, directions.left:directions.down, directions.right:directions.up}, 
         "\\":{directions.up:directions.left, directions.down:directions.right, directions.left:directions.up, directions.right:directions.down}}

def check_bounds(coords):
    if coords[0] < 0 or coords[0] >= len(input) or coords[1] < 0 or coords[1] >= len(input[0]):
        return False
    else:
        return True

import time
import os
def change(visited, count):
    if count % 2 == 0:
        visualizer.create_collage(input, visited).save(f"Day 16/images/{count}.png")
    return count + 1
def BFS(beam):
    input_copy = copy.deepcopy(input)
    beam_list = [beam]
    beam_cache = []
    visited = [[[] for y in range(len(input[0]))] for x in range(len(input))]
    count = 0
    while len(beam_list) > 0:
        beam_list[0].move()
        if not check_bounds(beam_list[0].coords):
            beam_list.pop(0)
            if len(beam_list) <= 1:
                beam_list += beam_cache
                beam_cache = []
                count = change(visited, count)
            continue
        input_copy[beam_list[0].coords[0]][beam_list[0].coords[1]] = "X"
        temp_char = input[beam_list[0].coords[0]][beam_list[0].coords[1]]  
        if (temp_char in ["|", "-"]):
            handle_splitter(temp_char, beam_list[0], beam_list, visited)
        elif (temp_char in ["/", "\\"]):
            beam_list[0].direction = special[temp_char][beam_list[0].direction]
        #if temp_char == ".":
        #os.system('cls')
        #for line in input_copy:
            #print("".join(line))
        if beam_list[0].direction in visited[beam_list[0].coords[0]][beam_list[0].coords[1]]:
            beam_list.pop(0)
            if len(beam_list) <= 1:
                beam_list += beam_cache
                beam_cache = []
                count = change(visited, count)
            continue
        #if directions.down in visited[4][4] or directions.up in visited[4][4]:
            #print("TWTSASD")
        visited[beam_list[0].coords[0]][beam_list[0].coords[1]].append(beam_list[0].direction)
        beam_cache.append(beam_list.pop(0))
        if len(beam_list) <= 1:
            beam_list += beam_cache
            beam_cache = []
            count = change(visited, count)
        
        #time.sleep(0.5)
        
    #print(input[beam_list[0].coords[0]][beam_list[0].coords[1]])

    #print(start_beam)
    xsum = 0
    for line in input_copy:
        xsum += line.count("X")
    return(xsum, visited)

def part1():
    start_beams = Beam((0,-1), directions.right)
    part1_sum, visited = BFS(start_beams)
    #print(visited[2][2])
    #print(visited[6][0], input[6][0])
    #visualizer.create_collage(input, visited).save("Day 16/images/visualizer.png")
    return part1_sum

def part2():
    max_sum = 0
    for x in range(len(input)):
        start_beam = Beam((x,-1), directions.right)
        max_sum = max(BFS(start_beam), max_sum)
        start_beam = Beam((x,len(input[0])), directions.left)
        max_sum = max(BFS(start_beam), max_sum)
    for x in range(len(input[0])):
        start_beam = Beam((-1,x), directions.down)
        max_sum = max(BFS(start_beam), max_sum)
        start_beam = Beam((len(input),x), directions.up)
        max_sum = max(BFS(start_beam), max_sum)
    return max_sum
print(part1())
