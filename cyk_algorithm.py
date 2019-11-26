"""
CYK Algorithm to testing whether a string is a membership of a CFL L
"""
from CFG2CNF import read_grammar
from CFG2CNF import read_terminal

def read_input_text(input_name):
    # Membaca file input dan mentimpannya dalam list
    input_file = open(input_name, 'r')
    input_file_lines = input_file.readlines()
    input_file.close()

    input_list = []

    for line in input_file_lines:
        linenew = line.replace("\n","")
        linenew = linenew.replace("    ","")
        input_list.append(linenew)

    return input_list

def cyk_algorithm(grammar, terminal_name, input_name):
    parse_table = None



    # Inisiasi input_string dan parse_table
    input_string = input_string.replace(" ","")
    length = len(input_string)
    parse_table = [[[] for x in range(length - y)] for y in range(length)]

    # Algoritma filling table:
    # BASIS: 
    # Isi terlebih dahulu baris pertama sesuai terminal dari input_string yang dibaca
    # tiap sel diisi dengan aturan produksi yang menghasilkan terminal tersebut
    for i, word in enumerate(input_string):
        for rule in grammar:
            if  rule[1] == word:    
                parse_table[0][i].append(rule[0])

    # Rekurens:
    # Misal kita ingin menentukan X[i][j] pada parse_table
    # kita telah mengisi X pada baris-baris di atasnya
    # Misal:
    # [['B'] ['A','C']]
    # [[A -> B A] [S -> B C] maka diisi ['A','S']]


    # Pertama, iterasi semua cell pada table
    for y in range(1,length):
        for x in range(length-y):
            for i in (parse_table[0][0]):
                for j in (parse_table[0][1]):
                    for rule in grammar:
                        if len(rule) > 2:
                            left = rule[1]
                            right = rule[2]
                            if left == i:
                                if right == j:
                                    print(rule[0])

    # for i in parse_table:
    #     print(i)

if __name__ == '__main__':
    # grammar = read_grammar('cnf.txt')
    grammar = [
    ["S", "A","B"],
    ["S", "B","C"],
    ["A", "B","A"],
    ["A", "a"],
    ["B", "C","C"],
    ["B", "b"],
    ["C", "A","B"],
    ["C", "a"]
    ]
    # cyk_algorithm(grammar,'input_test.txt')
    read_input_text('input_test.txt')