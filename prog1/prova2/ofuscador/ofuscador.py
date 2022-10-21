# UFCG - prog1
# Ismael R. da Silva Neto 121111104
# Recebe uma linha de código e a ofusca, transformando algumas letras em 'equivalentes' numéricos

def ofuscador(line):
    count = 0
    obfuscated = ''
    for e in line:
        if e != ' ':
            count += 1
        if e == ' ':
            e = '*' * count
            count = 0

        if e == 'A':
            e = 'a'
        elif e == 'B':
            e = 'b'
        elif e == 'C':
            e = 'c'
        elif e == 'D':
            e = 'd'
        elif e == 'E':
            e = 'e'
        elif e == 'F':
            e = 'f'
        elif e == 'G':
            e = 'g'
        elif e == 'H':
            e = 'h'
        elif e == 'I':
            e = 'i'
        elif e == 'J':
            e = 'j'
        elif e == 'K':
            e = 'k'
        elif e == 'L':
            e = 'l'
        elif e == 'M':
            e = 'm'
        elif e == 'N':
            e = 'n'
        elif e == 'O':
            e = 'o'
        elif e == 'P':
            e = 'p'
        elif e == 'Q':
            e = 'q'
        elif e == 'R':
            e = 'r'
        elif e == 'S':
            e = 's'
        elif e == 'T':
            e = 't'
        elif e == 'U':
            e = 'u'
        elif e == 'V':
            e = 'v'
        elif e == 'W':
            e = 'w'
        elif e == 'X':
            e = 'x'
        elif e == 'Y':
            e = 'y'
        elif e == 'Z':
            e = 'z'
        
        elif e == 'a':
            e = 'A'
        elif e == 'b':
            e = 'B'
        elif e == 'c':
            e = 'C'
        elif e == 'd':
            e = 'D'
        elif e == 'e':
            e = 'E'
        elif e == 'f':
            e = 'F'
        elif e == 'g':
            e = 'G'
        elif e == 'h':
            e = 'H'
        elif e == 'i':
            e = 'I'
        elif e == 'j':
            e = 'J'
        elif e == 'k':
            e = 'K'
        elif e == 'l':
            e = 'L'
        elif e == 'm':
            e = 'M'
        elif e == 'n':
            e = 'N'
        elif e == 'o':
            e = 'O'
        elif e == 'p':
            e = 'P'
        elif e == 'q':
            e = 'Q'
        elif e == 'r':
            e = 'R'
        elif e == 's':
            e = 'S'
        elif e == 't':
            e = 'T'
        elif e == 'u':
            e = 'U'
        elif e == 'v':
            e = 'V'
        elif e == 'w':
            e = 'W'
        elif e == 'x':
            e = 'X'
        elif e == 'y':
            e = 'Y'
        elif e == 'z':
            e = 'Z'

        if e == 'A' or e == 'a':
            e = '4'
        elif e == 'B' or e == 'b':
             e = '8'
        elif e == 'E' or e == 'e':
            e = '3'
        elif e == 'G' or e == 'g':
            e = '6'
        elif e == 'I' or e == 'i':
            e = '1'
        elif e == 'L' or e == 'l':
            e = '7'
        elif e == 'S' or e == 's':
            e = '5'
        elif e == 'O' or e == 'o':
            e = '0'

        elif e == '4':
            e = 'A'
        elif e == '8':
            e = 'B'
        elif e == '3':
            e = 'E'
        elif e == '6':
            e = 'G'
        elif e == '1':
            e = 'I'
        elif e == '7':
            e = 'L'
        elif e == '5':
            e = 'S'
        elif e == '0':
            e = 'O'
        obfuscated = f'{obfuscated}{e}'

    return obfuscated


def test_1():
    line = 'Questao grande!'
    assert obfuscated(line) == 'qU35T40*******6R4ND3!'


def test_2():
    line = 'Quase nao faço!'
    assert obfuscated(line) == 'qU453*****N40***F4C0!'


def test_3():
    line = 'ABEGILSO'
    assert obfuscated(line) == '48361750'


def test_4():
    line = '48361750'
    assert obfuscated(line) == 'ABEGILSO'

