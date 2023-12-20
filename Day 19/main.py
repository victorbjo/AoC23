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
    #rules_dict[ruleKey] = _rule_dict
#for ruleKey in rules_dict: #Rule printing
#    print(ruleKey, rules_dict[ruleKey])


#This is not working. This should be a somewhat recursive function that parses the rules and returns the result
#It needs to be done for each letter, and if a letter is not defined go straight to last rule




def parse_rule(rules, values):
        result = None
        if "<" in rule or ">" in rule: #Check if needs to compare
            letter = rule[0]#Parsing
            operator = rule[1]
            value = int(rule[2:rule.index(":")])
            happen = rule[rule.index(":")+1:]
            if operator == "<":#Compares
                if values[letter] < value:
                    result = happen
            elif operator == ">":
                if values[letter] > value:
                    result = happen
        else:#If not comparing, then just return the rule
            result = rule
        if result != None:#If there is a result, then it can be returned
            if result == "A" or result == "R":#If it is a accepted or rejected, then return bool
                return result == "A"
            else:
                return result #If not, then return the rule's consequence
def rule_in(rules, values, letter):
    rule = rules["in"]
    result = parse_rule(rule, values, letter)
    print("Result", result)

def parse_rule(ruleset, values, letter):
    #print("Parsing", ruleset, values, letter)
    value = values[letter]
    for rule in ruleset:
        result = None
        if type(rule) == str or type(rule) == bool:
            if type(rule) == bool:
                return rule
            result = parse_rule(rules_dict[rule], values, letter)
        elif rule[0] == letter:
            if rule[1] == "<":
                if value < rule[2]:
                    result = parse_rule(rules_dict[rule[3]], values, letter)
            elif rule[1] == ">":
                if value > rule[2]:
                    result = parse_rule(rules_dict[rule[3]], values, letter)
        if result == True or result == False:
            return result
rule_in(rules_dict, {"x":0,"m":1,"a":3400,"s":1350}, "s")
test = {"x":0,"m":1,"a":3400,"s":1350}
for key in test:
    #rule_in(rules_dict, {"x":0,"m":1,"a":3400,"s":1350}, key)
#Okay I did this slightly wrong. It should be done for each letter, and if perform each rule. As soon as R or A is returned, then return that
#Then sum XMAS rating if A and sum all sums