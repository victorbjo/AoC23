def part1():
    input = open("Day 07/input.txt").read().split("\n")
    card_lookup = {"A":14,"K":13,"Q":12,"J":11,"T":10}
    hand_types = [[] for _ in range(7)]
    def replace_chars(s_list):
        new_list = []
        for s in s_list:
            for key, value in card_lookup.items():
                s = s.replace(key, str(value))
            new_list.append(s)
        return new_list
    def count_unique(hand):
        return len(list(set(hand)))
    def count_sames(hand):
        sames = 0
        for char in hand:
            sames = max(sames, hand.count(char))
        return sames


    bid_dict = {}
    #[0] High card, 1 One pair, 2 Two pair, 3 Three of a, 4 Full House, 5 four of a, 6 five of a 
    for hand_raw in input:
        hand, bid = hand_raw.split()
        hand = replace_chars(list(hand))
        #print(count_unique(hand), "hand")
        uniques = (count_unique(hand))
        #bid_dict[hand] = bid
        if uniques == 5:
            hand_types[0].append(hand+ [bid])
        elif uniques == 4:
            hand_types[1].append(hand+ [bid])
        elif uniques == 3:
            if count_sames(hand) == 3:#Three of a kind
                hand_types[3].append(hand+ [bid])
            else: #Two pairs
                hand_types[2].append(hand+ [bid])
        elif uniques == 2:
            if count_sames(hand) == 3:#Full house
                hand_types[4].append(hand+ [bid])
            else:
                hand_types[5].append(hand+ [bid])
        else:
            hand_types[6].append(hand+ [bid])
    rank = 1
    sum = 0
    for type in hand_types:
        type_sorted = sorted(type, key=lambda x:  [int(x[i]) for i in range(6)])
        for hand in type_sorted:
            #print(hand, "RANK", rank, count_unique(hand[:-1]))
            sum += int(hand[-1])*rank
            rank += 1
    return(sum)



def part2():
    input = open("Day 07/input.txt").read().split("\n")
    card_lookup = {"A":14,"K":13,"Q":12,"J":0,"T":11}
    hand_types = [[] for _ in range(7)]
    def replace_chars(s_list):
        new_list = []
        for s in s_list:
            for key, value in card_lookup.items():
                s = s.replace(key, str(value))
            new_list.append(s)
        return new_list
    def count_unique(hand):
        uniques = len(list(set(hand)))
        if "0" in hand:
            uniques -= 1
        return uniques
    def count_sames(hand):
        sames = 0
        j = hand.count("0")
        for char in hand:
            if char != "0" : sames = max(sames, hand.count(char))
        sames += j
        return sames


    bid_dict = {}
    #[0] High card, 1 One pair, 2 Two pair, 3 Three of a, 4 Full House, 5 four of a, 6 five of a 
    for hand_raw in input:
        hand, bid = hand_raw.split()
        hand = replace_chars(list(hand))
        #print(count_unique(hand), "hand")
        uniques = (count_unique(hand))
        #bid_dict[hand] = bid
        if uniques == 5:
            #if "J" in hand:
                #hand_types[1].apped(hand + [bid])
            hand_types[0].append(hand+ [bid])
        elif uniques == 4:
            hand_types[1].append(hand+ [bid])
        elif uniques == 3:
            if count_sames(hand) == 3:#Three of a kind
                hand_types[3].append(hand+ [bid])
            else: #Two pairs
                hand_types[2].append(hand+ [bid])
        elif uniques == 2:
            if count_sames(hand) == 3:#Full house
                hand_types[4].append(hand+ [bid])
            else:
                hand_types[5].append(hand+ [bid])
        else:
            hand_types[6].append(hand+ [bid])
    rank = 1
    sum = 0
    for type in hand_types:
        type_sorted = sorted(type, key=lambda x:  [int(x[i]) for i in range(6)])
        for hand in type_sorted:
            #print(hand, "RANK", rank, count_unique(hand[:-1]))
            sum += int(hand[-1])*rank
            rank += 1
    print(sum)
    #print(count_unique(['0', '0', '0', '8', '0']))

part2()