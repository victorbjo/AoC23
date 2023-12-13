input = open("Day 13/input.txt", "r").read().split("\n\n")

def find_difference(list0, list1):
    list0 = "".join(list0)
    list1 = "".join(list1)
    return sum(1 for a, b in zip(list0, list1) if a != b)

def find_mirror_dimension(pattern, threshold=1):
    last_line = pattern[0]
    for x, sub_pattern in enumerate(pattern[1:]):
        if last_line == sub_pattern or find_difference(last_line, sub_pattern) == threshold:
            lower_match = x+2
            remainer = (len(pattern)) - lower_match
            pattern_length = min(x, remainer)
            start = (x)-pattern_length
            end = (x+1)+pattern_length+1#x+1 because of the shifted index of searched pattern, +1 because of the range function
            half_first = pattern[start:x+1]
            half_second = pattern[x+1:end]
            half_second.reverse()
            count = find_difference(half_first, half_second)
            if count == threshold:
                return x+1
        last_line = sub_pattern
    return None

def analyze_patterns(threshold = 0):
    task_sum = 0
    for pattern in input:
        split_pattern = pattern.split("\n")
        mirror = find_mirror_dimension(split_pattern, threshold)
        #print(mirror)
        if mirror == None:
            #print("No pattern found")
            rotated = list(zip(*split_pattern[::-1]))
            for x, line in enumerate(rotated):
                #print("".join(line))
                rotated[x] = "".join(line)
            rotated_mirror = find_mirror_dimension(rotated, threshold)
            task_sum += rotated_mirror
        else:
            task_sum += mirror*100
    return task_sum

def part1():
    return analyze_patterns(0)
def part2():
    return analyze_patterns(1)

print(part1())
print(part2())