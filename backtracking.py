#!/usr/bin/python

import sys

def readFile():
    arq = open('entrada.txt', 'r')
    texto = arq.readlines()[1:]
    for linha in texto :
        piecesList.append(linha.rstrip('\n'))
    arq.close()

if __name__== "__main__":
  piecesList = []
  readFile()
  print piecesList

