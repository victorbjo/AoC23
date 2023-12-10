def part_1():
    input = open("input.txt").read().split("\n")
    cubes = {"red":12,"green":13,"blue":14}
    sum = 0
    for x, game in enumerate(input):
        game_split = game[game.find(":")+1:].split(";")
        possible = True
        for draw in game_split:
            draw_split = draw.split(",")
            for draws in draw_split:
                if(int(draws[:3])>cubes[draws[3:].strip()]):
                    possible = False
        if possible:
            sum += x+1
        colors = {"red":0,"green":0,"blue":0}
    return sum

def part_2():
    #return
    input = open("input.txt").read().split("\n")
    sum = 0
    for x, game in enumerate(input):
        colors = {"red":0,"green":0,"blue":0}
        game_split = game[game.find(":")+1:].split(";")
        for draw in game_split:
            draw_split = draw.split(",")
            for draws in draw_split:
                colors[draws[3:].strip()] = max(colors[draws[3:].strip()],int(draws[:3]))
        sum += colors["blue"]*colors["green"]*colors["red"]
    return sum
print(part_2())