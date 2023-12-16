from math import lcm


def part1():
    input = open("Day 08/input.txt", "r").read().split("\n")
    directions = list(input.pop(0))
    directions_base = directions.copy()
    input.pop(0)
    next_node = 0
    nodes = []
    directions_list = []
    name_list = []
    for x, direction in enumerate(input):
        directions_list.append(direction[direction.index("(")+1:direction.index((")"))].split(","))
        name_list.append(direction[:direction.index("=")].strip())
        if name_list[-1][-1] == "A":
            nodes.append(name_list[-1])
    next_node = name_list.index("AAA")
    for x, char in enumerate(directions):
        if char == "L":
            next = directions_list[next_node][0].strip()
        else:
            next = directions_list[next_node][1].strip()
        next_node = name_list.index(next)
        if next == "ZZZ":
            return x+1
            break
        elif x == len(directions)-1:
            directions += directions_base
    


def part2():
    input = open("Day 08/input.txt", "r").read().split("\n")
    directions = list(input.pop(0))
    directions_base = directions.copy()
    input.pop(0)
    next_node = 0
    nodes = []
    directions_list = []
    name_list = []
    answers = []
    for x, direction in enumerate(input):
        directions_list.append(direction[direction.index("(")+1:direction.index((")"))].split(","))
        name_list.append(direction[:direction.index("=")].strip())
        if name_list[-1][-1] == "A":
            nodes.append(x)
    for node in nodes:
        next_node = node
        #print(next_node)
        for x, char in enumerate(directions):
            if char == "L":
                next = directions_list[next_node][0].strip()
            else: 
                next = directions_list[next_node][1].strip()
            next_node = name_list.index(next)
            if next[-1] == "Z":
                #print("Found ZZ", x+1)
                answers.append(x+1)
                break
            elif x == len(directions)-1:
                directions += directions_base
    return(lcm(*answers))
