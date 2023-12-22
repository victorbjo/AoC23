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


#Parsing of the data
xmas = []
for data_line in data:
    xmas_temp = {}
    data_line = data_line[1:-1].split(",")
    for data in data_line:
        data = data.split("=")
        xmas_temp[data[0]] = int(data[1])
    xmas.append(xmas_temp)

#This is not working. This should be a somewhat recursive function that parses the rules and returns the result
#It needs to be done for each letter, and if a letter is not defined go straight to last rule
def rule_in(rules, values):
    rule = rules["in"]
    result = parse_rule(rule, values)
    return result

def parse_rule(ruleset, values):
    #print("Parsing", ruleset, values)
    #value = values[letter]
    for rule in ruleset:
        result = None
        if type(rule) == str or type(rule) == bool:
            if type(rule) == bool:
                return rule
            result = parse_rule(rules_dict[rule], values)
        
        elif rule[1] == "<":
            if values[rule[0]] < rule[2]:
                if type(rule[3]) == bool:
                    return rule[3]
                result = parse_rule(rules_dict[rule[3]], values)
        elif rule[1] == ">":
            if values[rule[0]] > rule[2]:
                if type(rule[3]) == bool:
                    return rule[3]
                result = parse_rule(rules_dict[rule[3]], values)
        if result == True or result == False:
            return result
        
def part1():
    temp_sum = 0
    for dict_temp in xmas:
        if rule_in(rules_dict, dict_temp):
            for value in dict_temp.values():
                temp_sum += int(value)
    print(temp_sum)
print(4000*4000*4000*4000)