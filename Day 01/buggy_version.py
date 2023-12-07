def part_two():
    sum = 0
    numbers={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for x, line in enumerate(input):
        new_line = ""
        letters = ""
        keys_used = []
        for letter in line:
            if letter.isnumeric():
                new_line += str(letter)
                letters = ""
                keys_used = []
            else:
                letters += letter
                for key in numbers:
                    if key in letters and key not in keys_used:
                        new_line += str(numbers[key])
                        keys_used.append(key)
        print(new_line)
        temp_numbers = [num for num in new_line if num.isnumeric()]
        print(int(temp_numbers[0]+temp_numbers[-1]))
        sum += int(temp_numbers[0]+temp_numbers[-1])
    print(sum)