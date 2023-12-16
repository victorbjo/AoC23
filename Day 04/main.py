def part1():
    input = open("Day 04/input.txt", "r").read().split("\n")
    sum = 0
    for card in input:
        winning_nums = []
        winning_num_string = card[card.find(":")+1:card.find("|")]
        nums_string = card[card.find("|")+1:]
        nums = nums_string.split()
        winning_nums = winning_num_string.split()
        sum_temp = 1
        for num in winning_nums:
            if num in nums:
                sum_temp *= 2
        sum_temp /= 2
        if sum_temp >= 1:
            sum += sum_temp 
    return(sum)

def part2():
    input = open("Day 04/input.txt", "r").read().split("\n")
    sum = 0
    card_amount_queue = []
    for card in input:
        if card_amount_queue !=[]:
            card_amount = card_amount_queue.pop(0)+1
        else:
            card_amount = 1
        winning_nums = []
        winning_num_string = card[card.find(":")+1:card.find("|")]
        nums_string = card[card.find("|")+1:]
        nums = nums_string.split()
        winning_nums = winning_num_string.split()
        sum_temp = 0
        for num in winning_nums:
            if num in nums:
                sum_temp += 1
        for x in range(sum_temp):
            if x < len(card_amount_queue):
                card_amount_queue[x] += card_amount
            else:
                card_amount_queue.append(card_amount)
        sum += card_amount
    return(sum)


