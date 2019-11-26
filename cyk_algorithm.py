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

def cyk_algorithm_for_one_string(grammar, terminal_name, input_string):
    # Pengetesan sebuah input string dengan algoritma CYK
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

    # print(parse_table)

    # Rekurens:
    # Misal kita ingin menentukan X[i][j] pada parse_table
    # kita telah mengisi X pada baris-baris di atasnya
    # Misal:
    # [['B'] ['A','C']]
    # [[A -> B A] [S -> B C] maka diisi ['A','S']]
    # Pertama, iterasi semua cell pada table
    for x in range(1,length):
        for y in range(length-x):
            target = []
            i = x-1
            j = y
            while (len(target) != x+1):
                target.append(parse_table[i][j])
                if (i != 0):
                    i-=1
                else:
                    j+=1
            print(target)

def python_cyk_algorithm(grammar, terminal_name, input_name):
    input_list = read_input_text(input_name)
    terminal = read_terminal(terminal_name)
    cyk_algorithm_for_one_string(grammar, terminal, input_list[0])

if __name__ == '__main__':
    grammar = read_grammar('grammar.txt')
    python_cyk_algorithm(grammar, 'terminal_test.txt', 'input_test.txt')

    A = ["B","A"]
    B = ["B","a"]
    if A == B:
        print("HAI")