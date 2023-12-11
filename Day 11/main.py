input = open("Day 11/input.txt", "r").read().split("\n")
def rotate_2d_list_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
def rotate_2d_list_counterclockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def expand(list_to_expand):
    expanded_list = []
    for x, row in enumerate(list_to_expand):
        if all(char == "." or char == "v" for char in row):
            void_row = "v"*len(row)
            expanded_list.append(void_row)
        expanded_list.append(row)
    return expanded_list
#Expand list by rows, rotate 90 deg C, expand list by rows, rotate 90 deg CC
input=rotate_2d_list_counterclockwise(expand(rotate_2d_list_clockwise(expand(input))))
class Galaxy():
    def __init__(self, coords, id, multiplier = 2, map = input) -> None:
        self.coords = coords
        self.id = id
        self.map = map
        coords1 = self.get_voids_row()*multiplier+(self.coords[1]-self.get_voids_row()*2)
        coords0 = self.get_voids_col()*multiplier+(self.coords[0]-self.get_voids_col()*2)
        self.coords = (coords0, coords1)
    def get_voids_col(self):
        voids = 0
        for line in self.map[:self.coords[0]]:
            voids += line[0] == "v"
        return(voids)
    def get_voids_row(self):
        return "".join(self.map[0][:self.coords[1]+1]).count("v")
    def calc_dist(self, node0):
        return (abs(self.coords[0]-node0.coords[0])+abs(self.coords[1]-node0.coords[1]))
    def __repr__(self) -> str:
        return (f"Coords: {self.coords}, ID:{self.id}")
def get_sum(multi = 2):
    galaxy_counter = 0
    nodes : list[Galaxy] = []
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if str(char) == "#":
                nodes.append(Galaxy((x,y),galaxy_counter, multi))
                galaxy_counter += 1
    sum = 0
    for x, node in enumerate(nodes):
        for node0 in nodes[x+1:]:
            sum += node.calc_dist(node0)
    return(sum)
def part1():
    print(f"Part 1 {get_sum()}")
def part2():
    print(f"Part 2 {get_sum(1000000)}")
if __name__ == "__main__":
    part1()
    part2()