input = open("Day 15/input.txt", "r").read().split(",")
#current_hash = 0

def HASH(input):
    current_hash = 0
    for char in input:
        current_hash += ord(char)
        current_hash *= 17
        current_hash %= 256
    return current_hash

def part1():
    sum = 0
    for step in input:
        sum += HASH(step)
    return(sum) #Took 6 minutes? Fuck me

def part2():
    boxes:list[dict] = []
    for x in range(256):
        boxes.append({})
    for step in input:
        split = max(step.find("="), step.find("-"))
        split_value = step[split:split+1]
        letters = step[:split]
        hash_value = HASH(letters)
        if split_value == "=":
            number = step[split+1:]
            boxes[hash_value].update({letters:number})
        else:
            boxes[hash_value].pop(letters, None)
    part2_answer = 0
    for y, box in enumerate(boxes):
        for x, key in enumerate(box.keys()):
            #print(x+1, y+1, int(box[key]))
            temp_sum = (y+1) * (x+1) * int(box[key]) 
            part2_answer += temp_sum
    return(part2_answer)
part2()