input = open("Day 09/input.txt", "r").read().split("\n")
import time
def part1():
    sum = 0
    for x, line in enumerate(input):
        numbers = [line.split()]
        for number_set in numbers:
            new_nums = []
            for y, number in enumerate(number_set[:-1]):
                new_nums.append(int(number_set[y+1])-int(number))
            #print(new_nums, "New nums")
            numbers.append(new_nums)
            if (all(number == 0 for number in new_nums)):
                break
            #time.sleep(1)
        numbers.reverse()
        numbers[0].append(0)
        last_val = 0
        for number_set in numbers[1:]:
            last_val = last_val + int(number_set[-1])
            number_set.append(last_val)
        #print(last_val, "Last val")
        sum += last_val
    return sum



def part2():
    sum = 0
    for x, line in enumerate(input):
        numbers = [line.split()]
        for number_set in numbers:
            new_nums = []
            for y, number in enumerate(number_set[:-1]):
                new_nums.append(int(number_set[y+1])-int(number))
            #print(new_nums, "New nums")
            numbers.append(new_nums)
            if (all(number == 0 for number in new_nums)):
                break
            #time.sleep(1)
        numbers.reverse()
        numbers[0].append(0)
        last_val = 0
        #print(numbers)
        for number_set in numbers[1:]:
            #print(last_val, int(number_set[0]), "Before calc")
            last_val = int(number_set[0])-last_val
            #print(last_val, int(number_set[0]), "After calc")
            number_set.insert(0, last_val)
        sum += last_val
    return sum

#print(part1())
#print(part2())
