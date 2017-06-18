#!/usr/bin/python

import sys
import copy



def readFile():
    arq = open('entrada.txt', 'r')
    texto = arq.readlines()[1:]
    for linha in texto :
        piecesList.append(linha.rstrip('\n'))
    arq.close()

def flip(piece):
    flipped = list(reversed(piece['value']))
    piece['value'] =  flipped

    return piece



def match(pieces, piece):  
    for index, p in enumerate(pieces):               

        # nao compara peca da lista com peca original
        if piece['value'] != p['value']:

            # testa piece cm alguma da lista
            if piece['value'][-1] == p['value'][0]:
                return p

            flipped = flip(copy.copy(p))

            # testa piece cm alguma da lista virada
            if piece['value'][-1] == flipped['value'][0]:
                flipped['hasFlipped'] = True
                return flipped
    
    return None


def showSolution(game):
    output = ''
    for  item in game:
        output += ' ' + str(item['value'])
    
    print output

# remove imagem de peca adicionada
def removeYourImage(pieces, piece):
    flipped = flip(copy.copy(piece))

    for index, p in enumerate(pieces):       
        if flipped['value'] == p['value']:
            pieces.pop(index)
            break
        
    return

def remove(pieces, piece):
    for index, p in enumerate(pieces):
        if p['value'] == piece['value']:
            pieces.pop(index)
            break
    return

def contains(pieces, piece):    
    for p in pieces:
        flipped = flip(copy.copy (p))
        if flipped == piece:
            return True
        
    return False

def backtracking(pieces, n, currentList):       
    
    if len(currentList) == n:
        return currentList

    while True:
        matched = match(pieces, currentList[-1])

        if matched != None:
            currentList.append(matched)
            backtracking(pieces, n, currentList)

            print currentList
            exit(0)

        else:
            flipped = copy.copy(currentList[-1])
            pieces.append(flipped)

    return solution


solution = []
if __name__== "__main__":
 
    pieces = [
        {
            'value': [1, 2],
            'hasFlipped': False
        },
        {
            'value': [7, 4],
            'hasFlipped': False
        },
        {
            'value': [7, 2],
            'hasFlipped': False
        }       
    ]

    n = 3

    for piece in pieces:
        currentList = []
        currentList.append(piece)
        backtracking(pieces, n, currentList)
        currentList = []
      
       
    



