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
print(maps)

class Seed:
    def __init__(self, start, range):
        self.start = start
        self.range = range
        self.origin = start
        self.end = start+range
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
    print(pair)
for map in maps[:6]:
    for seed in seed_pairs:
        start_range = find_closest_range(seed.start, map)
        end_range = find_closest_range(seed.end, map)
        if start_range[0] == end_range[0]:
            seed.start = get_value(seed.start, map)
            seed.end = get_value(seed.end, map)
            if seed.start-seed.range == 0:
                print("HAT")
        else:
            EoS_range = max (int(start_range[0]+start_range[2]-1), 0)
            seed_pairs.append(Seed(EoS_range+1, seed.end-(EoS_range+1)))
            seed.end = EoS_range
            seed.start = get_value(seed.start, map)
            seed.end = get_value(seed.end, map)
            seed.range = seed.end-seed.start
        if (seed.range == 0): print(seed, "SEED")
        if map == maps[6]:
            break
print(maps[6])       
for pair in seed_pairs:
    print(pair)
print(find_closest_range(103, maps[0]))
