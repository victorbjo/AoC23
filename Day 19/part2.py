input = open("Day 19/input.txt", "r").read().split("\n\n")
rules = input[0].split("\n")
data = input[1].split("\n")
rules_dict = {}
for rule in rules:
    rule = rule.split("{")
    rules_dict[rule[0]] = rule[1][:-1].split(",")

#Hellish rule parsing. Will convert rules to a dictionary with the letter as key
for ruleKey in rules_dict:
    _rule_dict = {}
    for rule in (rules_dict[ruleKey]):
        if "<" in rule or ">" in rule:
            letter = rule[0]
            operator = rule[1]
            value = int(rule[2:rule.index(":")])
            happen = rule[rule.index(":")+1:]
            if happen == "A" or happen == "R":
                happen = happen == "A"
            rules_dict[ruleKey][rules_dict[ruleKey].index(rule)] = [letter, operator, value, happen]
            _rule_dict[letter] = [operator, value, happen]
        else:
            rule_value = rule
            if rule == "A" or rule == "R":
                rule_value = rule == "A"    
            rules_dict[ruleKey][rules_dict[ruleKey].index(rule)] = rule_value
            _rule_dict["end"] = rule_value




#This is not working. This should be a somewhat recursive function that parses the rules and returns the result
#It needs to be done for each letter, and if a letter is not defined go straight to last rule
def rule_in(rules, values):
    rule = rules["in"]
    result = parse_rule(rule, values)
    return result
A_pile = []
R_pile = []
def parse_rule(ruleset, values):
    #print("Parsing", ruleset, values)
    #value = values[letter]
    for rule in ruleset:
        result = None
        if type(rule) == str or type(rule) == bool:
            if type(rule) == bool:
                if rule:
                    A_pile.append(values)
                else:
                    R_pile.append(values)
            else:
                result = parse_rule(rules_dict[rule], values)
        
        elif rule[1] == "<":
            values_copy = values.copy()
            new_temp = values_copy.copy()
            #new_temp["ID"] = rule[0]
            new_temp[rule[0]] =[values_copy[rule[0]][0], min(rule[2]-1, values_copy[rule[0]][1])]
            if new_temp[rule[0]][0] > new_temp[rule[0]][1]:
                continue
            values[rule[0]] = [max(rule[2], values_copy[rule[0]][0]), values_copy[rule[0]][1]]
            if type(rule[3]) == bool:
                if rule[3]:
                    A_pile.append(new_temp)
                else:
                    R_pile.append(new_temp)
            else:
                parse_rule(rules_dict[rule[3]], new_temp.copy())
        elif rule[1] == ">":
            new_temp = values.copy()
            new_temp["ID"] = rule[0]
            new_temp[rule[0]] =[max(rule[2]+1, values[rule[0]][0]), values[rule[0]][1]]
            if new_temp[rule[0]][0] > new_temp[rule[0]][1]:
                continue
            values[rule[0]] = [values[rule[0]][0], min(rule[2], values[rule[0]][1])]
            if type(rule[3]) == bool:
                if rule[3]:
                    A_pile.append(new_temp)
                else:
                    R_pile.append(new_temp)
            else:
                parse_rule(rules_dict[rule[3]], new_temp.copy())
                
            #result = parse_rule(rules_dict[rule[3]], values)
        if result == True or result == False:
            return result
        
first_range = {"x":[1,4000], "m":[1,4000],"a":[1,4000],"s":[1,4000]}

rule_in(rules_dict, first_range)
#print("A:")
pos_sum = 0
for a in A_pile:
    #print(a)
    pos_sum += (a["x"][1]-a["x"][0]+1)* (a["m"][1]-a["m"][0]+1)* (a["a"][1]-a["a"][0]+1)* (a["s"][1]-a["s"][0]+1)
#print("R:")
#for r in R_pile:
#    print(r)

print(pos_sum)
#I think algorithm is working, but I need to remove overlapping ranges
