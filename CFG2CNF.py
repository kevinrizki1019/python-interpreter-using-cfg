def read_cfg_file(filename):
    file = open(filename, 'r')
    filelines = file.readlines()
    file.close()

    grammar = []
    
    for line in filelines:
        rule = line.replace(" ->", "").split()
        grammar.append(rule)

    for rule in grammar:
        # Memisahkan rule yang berbentuk X -> Y | Z
        try:
            or_idx = rule.index("|")

        except ValueError:
            or_idx = -1

        if (or_idx != -1):
            insertion_idx = grammar.index(rule) + 1
            nonterm = rule[0]
            rule_branch = [nonterm]
            for i in range(or_idx + 1, len(rule)):
                rule_branch.append(rule[i])
            for j in range(or_idx, len(rule)):
                rule.pop()
            grammar.insert(insertion_idx, rule_branch)
    
    return grammar
    # return [x.replace("->", "").split() for x in filelines]

def convert_large_rules(grammar):
    # Menangani grammar yang berbentuk A -> BCD menjadi A -> BX dan X -> CD
    # grammar is an array consisting of lines of array
    for rule in grammar:
        rule_index = grammar.index(rule) + 1
        if (len(rule) - 1) > 2:
            new_rule = []
            for i in range(2, len(rule)):
                new_rule.append(rule[i])
            for j in range(2, len(rule)):
                rule.pop()
            new_nonterm = new_rule[0] + "_new"
            rule.append(new_nonterm)
            new_rule.insert(0, new_nonterm)
            grammar.insert(rule_index, new_rule)

def convert_unit_productions(grammar):
    # Menangani grammar yang memiliki unit production, yaitu A -> B
    # grammar is an array consisting of lines of array
    for rule in grammar:
        if (len(rule) == 2):
            unit_production = rule[1]
            idxs_unit_production = search_rule(grammar, unit_production)
            for i in idxs_unit_production:
                grammar[i][0] = rule[0]
            grammar.remove(rule)
            


def search_rule(grammar, rule_nonterm):
    # Mengembalikan index dari rule dengan nonterm yang dicari dalam grammar
    # Diasumsikan rule tersedia dalam grammar
    idx_rule = []
    for i in range(0, len(grammar)):
        if grammar[i][0] == rule_nonterm:
            idx_rule.append(i)

    return idx_rule


def convert_grammar(filename):
    grammar = read_cfg_file(filename)
    for rule in grammar:
        if (len(rule) == 0):
            grammar.remove(rule)
    
    convert_unit_productions(grammar)
    convert_large_rules(grammar)
    for rule in grammar:
        print(rule)


# grammar = read_cfg_file('tes.txt')
# for rule in grammar:
#     print(rule)

convert_grammar('tes.txt')
