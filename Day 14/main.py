input = open("Day 14/input.txt", "r").read().split("\n")
input_copy = [list(line) for line in input]
import numpy as np
import hashlib

rock_list = []
rock_move_list = []
input_copy = np.array(input_copy)
def move_rock(x, y, list):
    if list[x - 1][y] == "." and x > 0:
        list[x][y] = "."
        list[x-1][y] = "O"
        return True
    return False

def tilt_north(array_to_tilt):
    moved = True
    while moved:
        temp_moved = False
        for x, line in enumerate(array_to_tilt):
            for y, char in enumerate(line):
                if char == "O":
                    #print("ROCK")
                    if move_rock(x, y, array_to_tilt):
                        temp_moved = True
        moved = temp_moved

def cycle(input = input_copy):
    array_to_cycle = input
    for x in range(4):
        tilt_north(array_to_cycle)
        array_to_cycle = np.rot90(array_to_cycle, -1)
    return array_to_cycle

def calculate_weight():
    weight = 0
    for x, line in enumerate(input_copy):
        weight += np.count_nonzero(line == "O")*(len(input_copy)-x)
    return weight
#cycle()
hashed_values = []
hashed_values.append(hashlib.sha256(input_copy.tobytes()).hexdigest())
for x in range(1000):
    print(x)
    input_copy = cycle()
    hashed = hashlib.sha256(input_copy.tobytes()).hexdigest()
    if hashed in hashed_values:
        print(x, "Hashed value found")
        #break
    else:
        hashed_values.append(hashed)
hashed_index = hashed_values.index(hashed)
loop = len(hashed_values) - hashed_index
cycles = 1000000000
cycles = hashed_index % loop
for x in range(cycles):
    input_copy = cycle()
print(cycles)
print(loop)
weight = calculate_weight()
print(weight)


for line in input_copy:
    print("".join(line))




#105208
