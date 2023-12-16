from enum import Enum
input = open("Day 16/input.txt", "r").read().split("\n")
input = [list(x) for x in input]
import copy
#input_copy = open("Day 16/input.txt", "r").read().split("\n")
#input_copy = [list(x) for x in input]
class directions(Enum):
    up = (-1,0)
    down = (1,0)
    left = (0,-1)
    right = (0,1)
class Beam:
    def __init__(self, coords, direction):
        self.coords = coords
        self.direction = direction
    def move(self):
        self.coords = (self.coords[0] + self.direction.value[0], self.coords[1] + self.direction.value[1])
    def __repr__(self) -> str:
        return f"Beam({self.coords}, Going {self.direction.name})"
    

def handle_splitter(char, beam, beam_list):
    if char == "|":
        if beam.direction == directions.up or beam.direction == directions.down:
            return
        else:
            beam.direction = directions.up
            beam_list.append(Beam(beam.coords, directions.down))
    elif char == "-":
        if beam.direction == directions.left or beam.direction == directions.right:
            return
        else:
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

def BFS(beam):
    input_copy = copy.deepcopy(input)
    beam_list = [beam]
    beam_cache = []
    visited = [[[] for y in range(len(input[0]))] for x in range(len(input))]

    while len(beam_list) > 0:
        beam_list[0].move()
        if not check_bounds(beam_list[0].coords):
            beam_list.pop(0)
            if len(beam_list) <= 1:
                beam_list += beam_cache
                beam_cache = []
            continue
        input_copy[beam_list[0].coords[0]][beam_list[0].coords[1]] = "X"
        temp_char = input[beam_list[0].coords[0]][beam_list[0].coords[1]]  
        if (temp_char in ["|", "-"]):
            handle_splitter(temp_char, beam_list[0], beam_list)
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
            continue
        visited[beam_list[0].coords[0]][beam_list[0].coords[1]].append(beam_list[0].direction)
        beam_cache.append(beam_list.pop(0))
        if len(beam_list) <= 1:
            beam_list += beam_cache
            beam_cache = []
        #time.sleep(0.5)
        
    #print(input[beam_list[0].coords[0]][beam_list[0].coords[1]])

    #print(start_beam)
    xsum = 0
    for line in input_copy:
        xsum += line.count("X")
    return(xsum)

def part1():
    start_beams = Beam((0,-1), directions.right)
    return BFS(start_beams)

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