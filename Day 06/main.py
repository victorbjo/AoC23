def part1():
    def calculate_distance(btn_time, race_time):
        dist = (race_time-btn_time)*btn_time
        return dist
    input = open("Day 06/input.txt", "r").read().split("\n")
    time = input[0].split(": ")[1].split()
    distance = input[1].split(": ")[1].split()
    race_time_product = 1
    for x, race in enumerate(distance):
        race_time_sum = 0
        for y in range(int(time[x])):
            if calculate_distance(int(y), int(time[x])) > int(race):
                race_time_sum += 1
        print(race_time_sum, "Sum part1")
        race_time_product*=race_time_sum
    print(race_time_product)
    pass



def part1_1():
    def calculate_distance(btn_time, race_time):
        dist = (race_time-btn_time)*btn_time
        return dist
    def binary_search(low_bound, high_bound, time, distance, lower = True):
        if high_bound-low_bound == 1:
            if calculate_distance(high_bound-1, time) == distance and not lower:
                return high_bound -1 
            return high_bound
        mid = (high_bound+low_bound)//2
        if (calculate_distance(mid, time) > distance and lower) or (lower == False and calculate_distance(mid, time) < distance):
            return binary_search(low_bound, mid, time, distance, lower)
        else:
            return binary_search(mid, high_bound, time, distance, lower)
    input = open("Day 06/input.txt", "r").read().split("\n")
    time = input[0].split(": ")[1].split()
    distance = input[1].split(": ")[1].split()
    race_time_product = 1
    for x, race in enumerate(distance):
        lowest_time = binary_search(0, int(time[x]), int(time[x]), int(race))
        highest_time = binary_search(0, int(time[x]), int(time[x]), int(race), False)
        race_time_sum = highest_time-lowest_time
        race_time_product*=race_time_sum
    print(race_time_product)



def part2_0():
    def calculate_distance(btn_time, race_time):
        dist = (race_time-btn_time)*btn_time
        return dist
    input = open("Day 06/input.txt", "r").read().split("\n")
    time = "".join(input[0].split(": ")[1].split())
    distance = "".join(input[1].split(": ")[1].split())
    race_time_sum = 0
    for y in range(int(time)):
        if calculate_distance(int(y), int(time)) > int(distance):
            race_time_sum += 1
    print(race_time_sum)
    pass
def part2_1():
    def calculate_distance(btn_time, race_time):
        dist = (race_time-btn_time)*btn_time
        return dist
    
    input = open("Day 06/input.txt", "r").read().split("\n")
    time = "".join(input[0].split(": ")[1].split())
    distance = "".join(input[1].split(": ")[1].split())
    race_time_sum = 0
    lower_bound = 0
    higher_bound = time
    for y in range(int(time)):
        if calculate_distance(int(y), int(time)) > int(distance):
            lower_bound = y
            break
    for y in range(int(time)):
        if calculate_distance(int(time)-int(y), int(time)) > int(distance):
            higher_bound = int(time)-int(y)
            break
    print(higher_bound-lower_bound)
    print(race_time_sum)
    pass

def part2_2():
    def calculate_distance(btn_time, race_time):
        dist = (race_time-btn_time)*btn_time
        return dist 
    def binary_search(low_bound, high_bound, time, distance, lower = True):
        if high_bound-low_bound == 1:
            return high_bound
        mid = (high_bound+low_bound)//2
        if (calculate_distance(mid, time) > distance and lower) or (lower == False and calculate_distance(mid, time) < distance):
            return binary_search(low_bound, mid, time, distance, lower)
        else:
            return binary_search(mid, high_bound, time, distance, lower)
    
    input = open("Day 06/input.txt", "r").read().split("\n")
    time = "".join(input[0].split(": ")[1].split())
    distance = "".join(input[1].split(": ")[1].split())
    lower = (binary_search(0, int(time), int(time), int(distance)))
    higher = (binary_search(0, int(time), int(time), int(distance), False))
    print(higher-lower)

#part1()
#Time the function part2
import time
start_time = time.time()
for x in range(1000):
    part1_1()
second_time = time.time()
for x in range(1000):
    part2_2()
print(f"Time for first task: {second_time-start_time} seconds, time for second task: {time.time()-second_time} seconds")