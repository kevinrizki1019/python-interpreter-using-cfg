def read_cfg_file(filename):
    file = open(filename, 'r')
    filelines = file.readlines()
    file.close()
    
    return [x.replace("->", "").split() for x in filelines]

def convert_large_rules(grammar):
    # grammar is an array consisting of lines of array
    for rule in grammar:
        grammar_index = grammar.index(rule) + 1
        if (len(rule) - 1) > 2:
            new_rule = []
            for i in range(2, len(rule)):
                new_rule.append(rule[i])
            for j in range(2, len(rule)):
                rule.pop()
            new_nonterm = new_rule[0] + "_new"
            rule.append(new_nonterm)
            new_rule.insert(0, new_nonterm)
            grammar.insert(grammar_index, new_rule)



def convert_grammar(filename):
    cfg_grammar = read_cfg_file(filename)
    for rule in cfg_grammar:
        if (len(rule) == 0):
            cfg_grammar.remove(rule)
    
    cnf_grammar = convert_large_rules(cfg_grammar)
    for rule in cfg_grammar:
        print(rule)


convert_grammar('tes.txt')
