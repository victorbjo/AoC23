input = open("Day 14/input.txt", "r").read().split("\n")
input_copy = [list(line) for line in input]
class Rock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.orig = (x,y)
    def move(self):
        if input[self.x - 1][self.y] == "." and self.x > 0:
            input_copy[self.x][self.y] = "."
            self.x -= 1
            input_copy[self.x][self.y] = "O"
            return True
        return False
    def different_move(self):
        if input_copy[self.x - 1][self.y] == "." and self.x > 0:
            self.x -= 1
            input_copy[self.x+1][self.y] = "."
            input_copy[self.x][self.y] = self
            return True
        return False
    def __repr__(self):
        return f"Rock({self.x}, {self.y})"
    def __str__(self) -> str:
        return "O"
rock_list = []
rock_move_list = []
'''for y, col in enumerate(input[0]):
    for x, line in enumerate(input):
        if line[y] == "O":
            rock_list.append(Rock(x, y))
            input_copy[x][y] = rock_list[-1]
            moved = True
            while moved:
                moved = rock_list[-1].different_move()'''

for x, line in enumerate(input):
    for y, char in enumerate(line):
        if char == "O":
            rock_list.append(Rock(x, y))
            rock_move_list.append(rock_list[-1])
            input_copy[x][y] = rock_list[-1]

moved = True
while moved:
    temp_moved = False
    for line in input_copy:
        for char in line:
            if isinstance(char, Rock):
                #print("ROCK")
                if char.different_move():
                    temp_moved = True
    moved = temp_moved


sum_part1 = 0
for rock in rock_list:
    sum_part1 += len(input_copy)-rock.x
print(sum_part1)
#for y, col in enumerate(input_copy[0]):
    #for line in input_copy:
        #if isinstance(line[y], Rock):
            #sum_part1 += len(input_copy)-
        #print(line)