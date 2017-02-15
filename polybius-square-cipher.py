# coding=utf-8
import sys, getopt
from string import ascii_lowercase
from collections import Counter
import numpy as np

##----TODO-------
#
#se ejecuta asi por ahora : python polybius-square-cipher.py -d -i mensaje.txt -o nada
#
#encriptar pasando por parámetro el keyword
#
##--------------

inputfile = ''
outputfile = ''
metodo = ''
#keyword = ''

def decrypt(ifile,ofile):
    diccionario = np.zeros((5,5))
    diccionario[0][0] = 'A'
    diccionario[0][1] = 'B'
    diccionario[0][2] = 'C'
    diccionario[0][3] = 'D'
    diccionario[0][4] = 'E'
    diccionario[1][0] = 'F'
    diccionario[1][1] = 'G'
    diccionario[1][2] = 'H'
    diccionario[1][3] = 'I/J'
    diccionario[1][4] = 'K'
    diccionario[2][0] = 'L'
    diccionario[2][1] = 'M'
    diccionario[2][2] = 'N'
    diccionario[2][3] = 'O'
    diccionario[2][4] = 'P'
    diccionario[3][0] = 'Q'
    diccionario[3][1] = 'R'
    diccionario[3][2] = 'S'
    diccionario[3][3] = 'T'
    diccionario[3][4] = 'U'
    diccionario[4][0] = 'V'
    diccionario[4][1] = 'W'
    diccionario[4][2] = 'X'
    diccionario[4][3] = 'Y'
    diccionario[4][4] = 'Z'
    
    with open(ifile) as mensaje:
        for line in mensaje:
            key = 0
            i = 0
            int1 = 0
            int2 = 0
            for c in line:
                i = i + 1
                if (i%2) == 0:
                    int2 = c
                    print int1,
                    print int2,
                    print diccionario[(int1 - 1)][(int2 - 1)]
                else:
                    int1 = c

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:cd", ["keyword=","ifile=","ofile="])
    except getopt.GetoptError:
        print 'polyalphabetic-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'polyalphabet-cipher.py -<metodo> -k <keyword> -i <inputfile> -o <outputfile OR "none">'
            sys.exit()
        elif opt == "-c":
            metodo = 'crypt'
        elif opt == "-d":
            metodo = 'decrypt'
        elif opt in ("-w", "--keyword"):
            keyword = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if metodo == 'decrypt':
        decrypt(inputfile,outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
