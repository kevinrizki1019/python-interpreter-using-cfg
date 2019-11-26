"""
CYK Algorithm to testing whether a string is a membership of a CFL L
"""
from CFG2CNF import read_grammar
from CFG2CNF import read_terminal

def separate_blank_from_terminal(input_file_lines):
    input_list_temp = []

    for linenew in input_file_lines:
        linenew = linenew.replace('(',' ( ')
        linenew = linenew.replace(')',' ) ')
        linenew = linenew.replace(':',' : ')
        linenew = linenew.replace('-',' - ')
        linenew = linenew.replace('+',' + ')
        linenew = linenew.replace('*',' * ')
        linenew = linenew.replace('/',' / ')
        linenew = linenew.replace('%',' % ')
        linenew = linenew.replace('=',' = ')
        linenew = linenew.replace('>',' > ')
        linenew = linenew.replace('<',' < ')
        linenew = linenew.replace(',',' , ')
        linenew = linenew.replace('.',' . ')
        linenew = linenew.replace('[',' [ ')
        linenew = linenew.replace(']',' ] ')
        linenew = linenew.replace('"',' " ')
        linenew = linenew.replace("'"," ' ")
        linenew = linenew.split()
        linenew.append('endline')
        input_list_temp.append(linenew)
        
    return input_list_temp

def read_input_text(input_name):
    # Membaca file input dan mentimpannya dalam list
    input_file = open(input_name, 'r')
    input_file_lines = input_file.readlines()
    input_file.close()

    input_list_temp = separate_blank_from_terminal(input_file_lines)

    input_list = []
    for element in input_list_temp:
        for string in element:
            input_list.append(string)

    return input_list

def token_to_object(token):
    # Object yang dimaksud disini adalah antara num, undef, atau word
    number = ['0','1','2','3','4','5','6','7','8','9']
    valid_variable_prefix = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','_']
    if token[0] not in valid_variable_prefix:
        if token[0] in number:
            for char in token[1:len(token)]:
                if char != '1' and char != '2' and char != '3' and char != '4' and char != '5' and char != '6' and char != '7' and char != '8' and char != '9'  and char != '0':
                    return "undef" # kasus kalo ada nama variabel yang diawali dengan angka
            return "num"
        else:
            return "undef"
    return "word"

def cyk_algorithm_for_one_string(grammar, terminal_list, input_list):
    # Pengetesan sebuah input string dengan algoritma CYK
    parse_table = None

    # print(terminal_list)
    print(input_list)
    skip_for_string = False
    for token in input_list:
        if skip_for_string:
            if (token == "'") or (token == '"'):
                skip_for_string = False
                continue
            idx = input_list.index(token)
            input_list.insert(idx, "word")
            input_list.remove(token)
            continue
        if token not in terminal_list:
            idx = input_list.index(token)
            result = token_to_object(token)
            input_list.insert(idx, result)
            input_list.remove(token)
        if token == "#":
            idx = input_list.index(token)
            iterate = idx
            original_len = len(input_list)
            while (iterate < original_len) and (input_list[idx] != 'endline'):
                input_list.remove(input_list[idx])
                iterate += 1
            if input_list[idx] == "endline":
                input_list.remove(input_list[idx])
        
        if token == "'":
            idx = input_list.index(token)
            if (input_list[idx + 1] == "'") and (input_list[idx + 2] == "'"):
                for i in range(3):
                    input_list.remove(input_list[idx])
                iterate = idx
                original_len = len(input_list)
                while (iterate < original_len) and ((input_list[idx] != "'") or (input_list[idx + 1] != "'") or (input_list[idx + 2] != "'")):
                    input_list.remove(input_list[idx])
                    iterate += 1
                if (input_list):
                    if (input_list[idx] == "'") and (input_list[idx + 1] == "'") and (input_list[idx + 2] == "'"):
                        for i in range(3):
                            input_list.remove(input_list[idx])
                else:
                    break

        if (token == "'") or (token == '"'):
            skip_for_string = True
    
    while ("endline" in input_list):
        input_list.remove("endline")
    print(input_list)
        


    # Inisiasi input_list dan parse_table
    length = len(input_list)
    parse_table = [[[] for x in range(length - y)] for y in range(length)]

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

    accepted = False
    for i in parse_table:
        print("Parse table:")
        print(i)
    for var in parse_table[length-1][0]:
        if var == 'ALGORITHM':
            print("Accepted")
            accepted = True
            break
    if not accepted:
        print("Syntax Error")
        
    

def python_cyk_algorithm(grammar, terminal_name, input_name):
    input_list = read_input_text(input_name)
    terminal, terminal_rule = read_terminal(terminal_name)
    cyk_algorithm_for_one_string(grammar, terminal, input_list)

if __name__ == '__main__':
    grammar = read_grammar('cnf.txt')
    input_file = input('Enter the input file to validate: ')
    python_cyk_algorithm(grammar, 'terminal.txt', input_file)

    A = ["B","A"]
    B = ["B","a"]
    if A == B:
        print("HAI")