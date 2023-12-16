import math
def part1():
    input = open("Day 03/input.txt", "r").read().split("\n")
    numbers = []
    numCoords = []
    symCoords = []
    #Find numbers and coords
    for x, line in enumerate(input):
        current_num = ""
        num_temp = []
        for y, char in enumerate(line):
            if char.isnumeric():
                current_num = current_num + str(char)
                num_temp.append([x, y])
            else:
                if char != ".":
                    symCoords.append([x, y])
                if current_num != "":
                    numbers.append([int(current_num), False])
                    current_num = ""
                    numCoords.append(num_temp)
                    num_temp = []
        if current_num != "":
            numbers.append([int(current_num), False])
            current_num = ""
            numCoords.append(num_temp)
            num_temp = []
    sum = 0
    
    #Check distance between numbers and symbols
    for x, coord in enumerate(symCoords):
        for x, numCoord in enumerate(numCoords):
            for num in numCoord:
                dist = math.sqrt(abs(coord[0] - num[0])**2 + abs(coord[1] - num[1])**2)
                if dist < 2:
                    numbers[x][1] = True
    #Add numbers that are near symbols
    for num in numbers:
        if num[1] == True:
            sum += num[0]
    return(sum)



def part2():
    input = open("Day 03/input.txt", "r").read().split("\n")
    numbers = []
    numCoords = []
    symCoords = []
    #Find numbers and coords
    for x, line in enumerate(input):
        current_num = ""
        num_temp = []
        for y, char in enumerate(line):
            if char.isnumeric():
                current_num = current_num + str(char)
                num_temp.append([x, y])
            else:
                if char == "*":
                    symCoords.append([x, y])
                if current_num != "":
                    numbers.append([int(current_num), False])
                    current_num = ""
                    numCoords.append(num_temp)
                    num_temp = []
        if current_num != "":
            numbers.append([int(current_num), False])
            current_num = ""
            numCoords.append(num_temp)
            num_temp = []
    sum = 0
    
    #Check distance between numbers and symbols
    for x, coord in enumerate(symCoords):
        nums_legal=[]
        for x, numCoord in enumerate(numCoords):
            num_legal = False
            for num in numCoord:
                dist = math.sqrt(abs(coord[0] - num[0])**2 + abs(coord[1] - num[1])**2)
                if dist < 2:
                    num_legal = True
                    numbers[x][1] = True
            if num_legal:
                nums_legal.append(numbers[x][0])
                #print(nums_legal)
        if len(nums_legal) == 2:
            sum += nums_legal[0] * nums_legal[1]


    return(sum)


