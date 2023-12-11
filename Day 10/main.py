input = open("Day 10/input.txt", "r").read().split("\n")
loop = [list(line) for line in input]

class pipe():
    def __init__(self, dist, type, coordinates) -> None:
        self.dist = dist
        self.type = type
        self.coordinates = coordinates
    def __str__(self) -> str:
        return f"Pipe: {self.type} at {self.coordinates} with distance {self.dist}"
for line in input:
    if line.count("S"):
        start = (input.index(line), line.index("S"))
print(start)
pipe_types = {
"|":[(-1,0),(1,0)], #is a vertical pipe connecting north and south. (0,0, top left corner)
"-":[(0,-1),(0,1)], #is a horizontal pipe connecting east and west.
"L":[(-1,0),(0,1)], #is a 90-degree bend connecting north and east.
"J":[(0,-1),(-1,0)], #is a 90-degree bend connecting north and west.
"7":[(0,-1),(1,0)], #is a 90-degree bend connecting south and west.
"F":[(1,0),(0,1)], #is a 90-degree bend connecting south and east.
".":[], #is ground; there is no pipe in this tile.
",":[], #is ground; there is no pipe in this tile.
"S":[(0,1),(0,-1),(1,0),(-1,0)], #is the starting tile, located at row 0, column 0.
}
def check_compat(pipe0, pipe1):
    new_coords = (pipe0.coordinates[0]-pipe1.coordinates[0], pipe0.coordinates[1]-pipe1.coordinates[1])
    #print(new_coords)
    #print(pipe_types[pipe1.type])
    return new_coords in pipe_types[pipe1.type]
def breath_first_search(start, loop = loop):
    pipes_visited = []
    pipes_q = [start]
    max_dist = 0
    while pipes_q:
        current_pipe = pipes_q.pop(0)
        if current_pipe.coordinates in pipes_visited:
            continue
        max_dist = max(max_dist, current_pipe.dist)
        pipes_visited.append(current_pipe.coordinates)
        #pipes_visited.append(current_pipe)
        for pipe_type in pipe_types[current_pipe.type]:
            new_coords = (current_pipe.coordinates[0]+pipe_type[0], current_pipe.coordinates[1]+pipe_type[1])
            if new_coords[0] < 0 or new_coords[1] < 0 or new_coords[0] >= len(loop) or new_coords[1] >= len(loop[0]):
                continue
            if loop[new_coords[0]][new_coords[1]] != ".":
                new_pipe = pipe(current_pipe.dist+1, loop[new_coords[0]][new_coords[1]], new_coords)
                if check_compat(current_pipe, new_pipe):
                    pipes_q.append(new_pipe)
                #print(new_pipe,check_compat(current_pipe, new_pipe))
        #time.sleep(4)
        #print(current_pipe.dist, current_pipe.coordinates, current_pipe.type)
    return(max_dist, pipes_visited)
def part1(): #Breadth first search
    start_pipe = pipe(0, "S", start)
    return breath_first_search(start_pipe)[0]
#print(part1())

replace = {
    "L": [[",","|",","],[",","L","-"],[",",",",","]],
    "7": [[",",",",","],["-","7",","],[",","|",","]],
    "J": [[",","|",","],["-","J",","],[",",",",","]],
    "F": [[",",",",","],[",","F","-"],[",","|",","]],
    "|": [[",","|",","],[",","|",","],[",","|",","]],
    "-": [[",",",",","],["-","-","-"],[",",",",","]],
    ".": [[",",",",","],[",",".",","],[",",",",","]],
    "S": [[",","|",","],["-","S","-"],[",","|",","]],
}

def part2():
    start_pipe = pipe(0, "S", start)
    loop_visited = breath_first_search(start_pipe)[1]
    print("Breath first search done")
    horizontal = [] #Lists used to start search
    vertical = [] #Basically go out from these points, if they are not part of loop visited, then add to list
    for i in range(2):
        for x in range(len(loop)):
            vertical.append((x, i*(len(loop[0])-1)))
        for x in range(len(loop[0])):
            horizontal.append((i*(len(loop)-1),x))
    visited = []
    queue = [*horizontal.copy()+vertical.copy()]
    #print(queue)
    count = 0
    directions = (0,1),(0,-1),(1,0),(-1,0)
    while queue:
        current_tile = queue.pop(0)
        if current_tile in visited or current_tile in loop_visited:
            continue
        #if current_tile == (6,7):
           # print("Found111")
        #if current_tile == (7,8):
            #print("Found")
        visited.append(current_tile)
        count += loop[current_tile[0]][current_tile[1]] == "."
        if loop[current_tile[0]][current_tile[1]] == ".":
            loop[current_tile[0]][current_tile[1]] = "O"
        if current_tile in [(3,3), (2,4), (2,2), (1,3)]:
            print("Found", current_tile)
        for direction in directions:
            new_coords = (current_tile[0]+direction[0], current_tile[1]+direction[1])
            if new_coords[0] < 0 or new_coords[1] < 0 or new_coords[0] >= len(loop) or new_coords[1] >= len(loop[0]):
                continue
            if new_coords == (6,8):
                print("Found", current_tile)
            queue.append(new_coords)
    for line in loop:
        print("".join(line))
    print(count)

#part2()
new_loop = [["0" for x in range(len(loop[0])*3)] for x in range(len(loop)*3)]
for x in range(len(loop)):
    for y in range(len(loop[0])):
        for i in range(3):
            for j in range(3):  
                new_loop[x*3+i][y*3+j] = replace[loop[x][y]][i][j]
for line in new_loop:
    print("".join(line))

loop0 = loop
def part2(loop = new_loop):
    print("Starting part 2")
    start_pipe = pipe(0, "S", (start[0]*3+1, start[1]*3+1))
    loop_visited = breath_first_search(start_pipe, new_loop)[1]
    print("Breath first search done")
    horizontal = [] #Lists used to start search
    vertical = [] #Basically go out from these points, if they are not part of loop visited, then add to list
    for i in range(2):
        for x in range(len(loop)):
            vertical.append((x, i*(len(loop[0])-1)))
        for x in range(len(loop[0])):
            horizontal.append((i*(len(loop)-1),x))
    visited = []
    queue = [*horizontal.copy()+vertical.copy()]
    #print(queue)
    count = 0
    directions = (0,1),(0,-1),(1,0),(-1,0)
    print("Starting loop")
    while queue:
        current_tile = queue.pop(0)
        if current_tile in visited or current_tile in loop_visited:
            continue
        #if current_tile == (6,7):
           # print("Found111")
        #if current_tile == (7,8):
            #print("Found")
        visited.append(current_tile)
        count += loop[current_tile[0]][current_tile[1]] == "."
        if loop[current_tile[0]][current_tile[1]] == ".":
            loop[current_tile[0]][current_tile[1]] = "O"
        loop[current_tile[0]][current_tile[1]] = "O"
        for direction in directions:
            new_coords = (current_tile[0]+direction[0], current_tile[1]+direction[1])
            if new_coords[0] < 0 or new_coords[1] < 0 or new_coords[0] >= len(loop) or new_coords[1] >= len(loop[0]):
                continue
            queue.append(new_coords)
    print("Done")
    for char in loop_visited:
        new_loop[char[0]][char[1]] = "X"
    for line in loop:
        print("".join(line))
    print(count)
    dots = 0
    print(dots)
    new_list = []
    for x in range(1, len(new_loop), 3):
        new_list.append([])
        for y in range(1, len(new_loop[0]), 3):
            if new_loop[x][y] not in ["X", "O", ","]:
                new_list[-1].append("k")
                dots += 1
            elif new_loop[x][y] == "X":
                new_list[-1].append(loop0[int(x/3)][int(y/3)])
                #dots += 1
            else:
                new_list[-1].append("O")
            
    print(dots)
    for line in new_list:
        print("".join(line))
    print(new_list)
    import visualizer
    collage = visualizer.create_collage(new_list)
    collage.show()
part2()
