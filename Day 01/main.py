#Started 7:52
input = open("Day 01/input.txt","r").read().split("\n")
sum = 0
def part1():
    sum = 0
    for x, line in enumerate(input):
        temp_numbers = [num for num in line if num.isnumeric()]
        sum += int(temp_numbers[0]+temp_numbers[-1])
    return(sum)

def part2():
    sum = 0
    numbers={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for x, line in enumerate(input):
        new_line = ""
        letters = ""
        for letter in line:
            if letter.isnumeric():
                new_line += str(letter)
                letters = ""
            else:
                letters += letter
                for key in numbers:
                    if key in letters:
                        letters = letters[-1:]
                        new_line += str(numbers[key])
        sum += int(new_line[0]+new_line[-1])
    return(sum)
#part_one()
#part_two()