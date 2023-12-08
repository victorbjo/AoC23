input = open("input2.txt", "r").read().split("\n\n")

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
        if value < line[0]+line[2] and value >= line[0]:
            return map[x]
    return [0, 0, 0]
def get_value(value, map):
    map_temp = find_closest_range(value, map)
    if value > map_temp[0]+map_temp[2] or value < map_temp[0]:
        return value
    else:
        return (map_temp[1]-map_temp[0])+value
#print(maps)

class Seed:
    def __init__(self, start, range):
        self.start = start
        self.range = range
        self.origin = start
        self.end = start+range
        self.changes = 0
    def __repr__(self):
        return f"Seed: {self.start} - {self.end}. Origin: {self.origin}, Range: {self.range}"
    
seed_pairs : [Seed] = [Seed(int(seeds[x]), int(seeds[x+1])) for x in range(0, len(seeds), 2)]
#print(seed_pairs)
#Should I convert seeds pairs to a dict?
#Then you can do like this [{origSeedValue: destSeedValue, maxSeedValue: maxSeedValue},...]
#Makes it easy to track (When finished) and easy to add new when you have to split seeds
#Does it make sense to merge seeds again? Probably not, depends on amount of seeds after each round
#print()
for pair in seed_pairs:
    pass
    #print(pair)
num = 0
import time

print("SEEDS")
print(len(seed_pairs))
print(len(maps[0]))
print(len(maps[1]))
print(len(maps[2]))
print(len(maps[3]))
print(len(maps[4]))
print(len(maps[5]))
print(len(maps[6]))
new_seed_pairs = []
for x,map in enumerate(maps[:6]):
    print(len(seed_pairs))
    print("MAP"), x
    print(len(new_seed_pairs))
    for seed in seed_pairs:
        if len(seed_pairs) % 1000:
            print(len(seed_pairs))
        start_range = find_closest_range(seed.start, map)
        end_range = find_closest_range(seed.end, map)
        if start_range == end_range:
            seed.start = get_value(seed.start, map)
            seed.end = get_value(seed.end, map)
            seed.changes += 1
        else:
            seed.changes += 1
            if seed.changes > 22: #seed.start == 1526291750 and seed.end == 1803056005 
                1506703078 - 1568473870
                1584043708 - 1808006977
                print("HERE MF")
                print(start_range, end_range)
                break
            EoS_range = max (int(start_range[0]+start_range[2]-1), 0)
            num += 1
            new_seed_pairs.append(Seed(EoS_range+1, seed.end-(EoS_range+1)))
            if seed_pairs[-1].range == 0:
                seed_pairs.pop()

            seed.end = EoS_range
            seed.start = get_value(seed.start, map)
            seed.end = get_value(seed.end, map)
            seed.range = seed.end-seed.start
            if x > 1:
                time.sleep(5)
    if map == maps[1]:
        break
print("HERE")
for x in new_seed_pairs:
    print(x)
#print(maps[6])       
for pair in seed_pairs:
    pass
    #print(pair)
#print(find_closest_range(103, maps[0]))

