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

    input_list_temp = []


    for line in input_file_lines:
        linenew = line.replace('(',' ( ')
        linenew = linenew.replace(')',' ) ')
        linenew = linenew.replace(':',' : ')
        linenew = linenew.split()
        input_list_temp.append(linenew)
    
    input_list = []
    for element in input_list_temp:
        for string in element:
            input_list.append(string)

    return input_list

def cyk_algorithm_for_one_string(grammar, terminal_list, input_list):
    # Pengetesan sebuah input string dengan algoritma CYK
    parse_table = None

    print(terminal_list)
    for i in input_list:
        if i not in terminal_list:
            idx = input_list.index(i)
            input_list.insert(idx, 'word')
            input_list.remove(i)

    # Inisiasi input_list dan parse_table
    length = len(input_list)
    parse_table = [[[] for x in range(length - y)] for y in range(length)]

    print(input_list)
    # Algoritma filling table:
    # BASIS: 
    # Isi terlebih dahulu baris pertama sesuai terminal dari input_list yang dibaca
    # tiap sel diisi dengan aturan produksi yang menghasilkan terminal tersebut
    

    for i, token in enumerate(input_list):
        exist = False
        for rule in grammar:
            if  rule[1] == token:    
                exist = True
                parse_table[0][i].append(rule[0])
        if not exist:
            parse_table[0][i].append('WORD')


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

            left_x = 0
            right_x = x - 1
            right_y = y + 1

            while (left_x < x and right_x >= 0):
                left = parse_table[left_x][y]
                right = parse_table[right_x][right_y]
                
                left_cell = [n for n in left]
                right_cell = [n for n in right]
                
                for one in left_cell:
                    for two in right_cell:
                        target = []
                        target.append(one)
                        target.append(two)

                        for rule in grammar:
                            if (target == rule[1:3]) and (rule[0] not in parse_table[x][y]):
                                parse_table[x][y].append(rule[0])
                right_y += 1
                left_x += 1
                right_x -= 1

    for i in parse_table:
        print(i)
    # for var in parse_table[length-1][0]:
    #     if var == 'S':
    #         print("accepted")
    #         break
        
    

def python_cyk_algorithm(grammar, terminal_name, input_name):
    input_list = read_input_text(input_name)
    terminal, terminal_rule = read_terminal(terminal_name)
    cyk_algorithm_for_one_string(grammar, terminal, input_list)

if __name__ == '__main__':
    grammar = read_grammar('cnf.txt')
    python_cyk_algorithm(grammar, 'terminal.txt', 'input.txt')

    A = ["B","A"]
    B = ["B","a"]
    if A == B:
        print("HAI")