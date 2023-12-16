input = open("Day 05/input.txt", "r").read().split("\n\n")

seeds = []
seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_loc = []
lists = [seeds, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc]
maps = []
for x in range(8):
    maps.append([])
for x, line in enumerate(input):
    lists[x] = line.split("\n")
for x, list in enumerate(lists[1:8]):
    for line in list[1:]:
        line = line.split(" ")
        #First value is origin second is destination and third is span. Real numbers are Dest, Origin, Span
        maps[x+1].append([int(line[1]),int(line[0]), int(line[2])])
    #Sort by first value
    maps[x+1].sort(key=lambda z: z[0])
seeds = lists[0][0][7:].split()
#print(seeds)
maps = maps[1:]
def find_closest_range(value, map):
    for x, line in enumerate(map):
        if value < line[0]:
            return map[x-1]
    return map[-1]
def get_value(value, map):
    map_temp = find_closest_range(value, map)
    if value > map_temp[0]+map_temp[2] or value < map_temp[0]:
        return value
    else:
        return (map_temp[1]-map_temp[0])+value
def part1():
    scores = []
    for seed in seeds:
        temp_val = int(seed)
        for x in range(len(maps)):
            temp_val = get_value(temp_val, maps[x])
        scores.append([temp_val, seed])
    scores.sort(key=lambda z: z[0])
    return(scores)
combos = 1865197342
def part2():
    import time
    tests = 0
    timer0 = time.time()
    score = 10000000000
    for x in range(0, len(seeds),2):
        for y in range(int(seeds[x]), int(seeds[x+1])+int(seeds[x])):
            tests += 1
            temp_val = y
            for x in range(len(maps)):
                temp_val = get_value(temp_val, maps[x])
            score = min(temp_val, score)
            if tests%1000000 == 0:
                timer2 = time.time()
                #print(f"{round(tests/combos*100,4)}% in {round(timer2-timer0, 2)} seconds. ")
    return(score)
part2()