from collections import Counter

value = dict(zip('23456789TJQKA', range(13)))
value2 = dict(zip('J23456789TQKA', range(13)))

def score(i):
    return sorted(Counter(i[0]).values(), reverse=True), [value[c] for c in i[0]]

def score2(i):
    if i[0] == 'JJJJJ':
        hand_type = [5,]
    else:
        c = Counter(i[0])
        jokers = c.pop('J', 0)
        hand_type = sorted(c.values(), reverse=True)
        hand_type[0] += jokers

    return hand_type, [value2[c] for c in i[0]]

data = [line.split() for line in open('input.txt')]
#print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=score))))
print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=score2))))
