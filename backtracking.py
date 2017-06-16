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


# compara number com os primeiro lados da peca de domino
def match(p1, p2):
    return p1['value'][1] == p2['value'][0]

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

def contains(pieces, piece):    
    for p in pieces:
        flipped = flip(copy.copy (p))
        if flipped == piece:
            return True
        
    return False


def backtracking(pieces, n, solution):   

    if (len(solution) == n):
        showSolution(solution)   
        exit(1)

    if len(solution) == 0:
        currentPiece = pieces.pop(0)
        solution.append(currentPiece)       

    i = 0
    while len(pieces) > 0:
        piece = pieces[i]
        
        # pode encaixar? remove peca adicionada e remove sua imagem tbm
        if match(solution[-1], piece) and contains(pieces, piece) == False:
            solution.append(piece)
            image = pieces.pop(i)
            removeYourImage(pieces, image)                        
            i = 0
            backtracking(pieces, n, solution)
            
        # se nao deu match e nao foi flipado ainda, adiciona peca virada a lista
        elif piece['hasFlipped'] == False:
            flipped = copy.copy(piece)
            flipped = flip(flipped)
            flipped['hasFlipped'] = True

            pieces.append(flipped)
        

        i += 1

    return []


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
        },
        {
            'value': [4, 6],
            'hasFlipped': False
        },
        {
            'value': [0, 6],
            'hasFlipped': False
        }
    ]

    n = 5

    for piece in pieces:
        solution = []
        solution = backtracking(pieces, n, solution)

        if len(solution) > 0:
            showSolution(solution)
            break
    



