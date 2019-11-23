"""
CYK Algorithm to testing whether a string is a membership of a CFL L
"""

grammar = None
table = None
input_string = "b a a b a"

# Simpan Grammar sebagai suatu struktur data
grammar = [
  ("S", ["A","B"]),
  ("S", ["B","C"]),
  ("A", ["B","A"]),
  ("A", ["a"]),
  ("B", ["C","C"]),
  ("B", ["b"]),
  ("C", ["A","B"]),
  ("C", ["a"])
]

# Inisiasi input_string dan parse_table
input_string = input_string.replace(" ","")
length = len(input_string)
parse_table = [[[] for x in range(length - y)] for y in range(length)]

# Algoritma filling table:
# BASIS: 
# Isi terlebih dahulu baris pertama sesuai terminal dari input_string yang dibaca
# tiap sel diisi dengan aturan produksi yang menghasilkan terminal tersebut
for i, word in enumerate(input_string):
    for LHS, RHS in grammar:
        for RHS_word in RHS:
            if RHS_word == word:    
                parse_table[0][i].append(LHS)

# Rekurens:
# Misal kita ingin menentukan X[i][j] pada parse_table
# kita telah mengisi X pada baris-baris di atasnya
# Misal:
# [['B'] ['A','C']]
# [[A -> B A] [S -> B C]]

# for i in range(1,length):
#     for j in range(0,length-i):   

for i in parse_table:
    print(i)