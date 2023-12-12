input = open("Day 12/input.txt", "r").read().split("\n")
import time
from functools import cache

@cache
def check(spring_set : list, chart_set: list, counter = 0, active = False):
        #print(spring_set, chart_set, counter, active)
        #time.sleep(0)
        if len(spring_set) == 0:
            if "#" in chart_set:
                #print(0)
                return 0
            #print("Found", counter)
            #print(1)
            return 1
        elif len(chart_set) == 0:
            #print(0)
            return 0
        if chart_set[0] == ".":
            if active:
                #print(0)
                return 0
            temp_sum = check(spring_set, chart_set[1:], counter = counter+1)
        elif chart_set[0] =="#":
            if active == None:
                #print(0)
                return 0
            spring_copy = spring_set.copy()
            spring_copy[0] -= 1
            #print(spring_set, "Sprint set")
            if spring_copy[0] == 0:
                temp_sum = check(spring_copy[1:], chart_set[1:], counter+1, active = None)
            else:
                temp_sum = check(spring_copy, chart_set[1:], counter+1, active = True)
        elif chart_set[0] == "?":
            chart_set_copy0 = chart_set.copy()
            chart_set_copy0[0] = "."
            temp_sum = check(spring_set, chart_set_copy0, counter = counter+1, active=active)
            chart_set_copy1 = chart_set.copy()
            chart_set_copy1[0] = "#"
            temp_sum += check(spring_set, chart_set_copy1, counter = counter+1,active=active)
        return temp_sum

sum = 0
for x, line in enumerate(input):
    print(x)
    chart, springs = line.split(" ")
    chart += "?"
    chart *= 5
    chart = chart[:-1]
    springs += ","
    springs *= 5
    springs = springs[:-1]
    springs = springs.split(",")
    springs = list(map(int, springs))
    #chart = chart.split(".")
    chart = list(chart)
    #print(springs)
    #print(chart, "CHART")
    known_springs = []
    temp_springs = []
    #print("")

    sum += check(springs, chart)
print(sum)
    
    
