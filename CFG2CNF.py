def read_terminal(filename):
    # Membaca file terminal dan menyimpannya dalam list character
    terminalfile = open(filename, "r")
    terminaltemp = terminalfile.readlines()
    terminalfile.close()

    terminal = []
    for line in terminaltemp:
        linenew = line.replace("\n", "")
        terminal.append(linenew)

    return terminal

def read_grammar(filename):
    # Membaca file grammar dalam bentuk production rule A -> B C D 
    # dan mengubahnya menjadi bentuk ['A', 'B', 'C', 'D']
    file = open(filename, 'r')
    filelines = file.readlines()
    file.close()

    grammar = []
    
    for line in filelines:
        rule = line.replace(" ->", "").split()
        grammar.append(rule)

    for rule in grammar:
        # Memisahkan rule yang berbentuk X -> Y | Z menjadi X -> Y dan X -> Z
        try:
            or_idx = rule.index("|")

        except ValueError:
            # Apabila sebuah nonterminal tidak mengandung 2 production rule yang berbeda
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
    # Menangani production rule yang berbentuk A -> BCD menjadi A -> BX dan X -> CD
    addition = 1
    for rule in grammar:
        rule_index = grammar.index(rule) + 1
        if (len(rule) - 1) > 2:
            new_rule = []
            for i in range(2, len(rule)):
                new_rule.append(rule[i])
            for j in range(2, len(rule)):
                rule.pop()
            new_nonterm = new_rule[0] + "_deriv"
            for checkrule in grammar:
                if checkrule[0] == new_nonterm:
                    new_nonterm += "{}".format(addition)
                    addition += 1
                    break
            rule.append(new_nonterm)
            new_rule.insert(0, new_nonterm)
            if new_rule not in grammar:
                grammar.insert(rule_index, new_rule)

def convert_unit_productions(grammar):
    # Menangani grammar yang memiliki unit production, yaitu A -> B
    # grammar is an array consisting of lines of array
    terminal = read_terminal('terminal.txt')
    
    j = 0
    while j < len(grammar):
        if ((len(grammar[j]) == 2) and (grammar[j][1] not in terminal)):
            unit_production = grammar[j][1]
            idxs_unit_production = search_rule(grammar, unit_production)
            for i in idxs_unit_production:
                new_rule = []
                for termnonterm in grammar[i]:
                    new_rule.append(termnonterm)
                new_rule[0] = grammar[j][0]
                grammar.insert(j + 1, grammar[i])
            grammar.remove(grammar[j])
        j += 1


def search_rule(grammar, rule_nonterm):
    # Mengembalikan index dari rule dengan nonterm yang dicari dalam grammar
    # Diasumsikan rule tersedia dalam grammar
    idx_rule = []
    for i in range(0, len(grammar)):
        if grammar[i][0] == rule_nonterm:
            idx_rule.append(i)

    return idx_rule

def write_to_file(grammar):
    # Menuliskan grammar dalam bentuk A -> B C dalam file .txt

    for rule in grammar:
        for line in grammar:
            if rule[0] == line[0] :
                if (grammar.index(rule) != grammar.index(line)):
                    rule.append("|")
                    for i in range(1, len(line)):
                        rule.append(line[i])
                    grammar.remove(line)
            


    filename = raw_input("Enter the output file name: ")
    file = open(filename, 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" ->")
        for i in range(1, len(rule)):
            file.write(" {}".format(rule[i]))
        file.write("\n")
    file.close()


def convert_grammar(filename):
    grammar = read_grammar(filename)
    for rule in grammar:
        if (len(rule) == 0):
            grammar.remove(rule)
    
    convert_unit_productions(grammar)
    convert_large_rules(grammar)
    # for rule in grammar:
    #     print(rule)
    write_to_file(grammar)

if __name__ == '__main__':
    filename = raw_input("Enter the Context Free Grammar file to convert: ")
    convert_grammar(filename)

