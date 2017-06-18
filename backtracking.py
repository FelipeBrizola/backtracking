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

def showPiece(piece, value):
    string = str(piece['left'])+","+str(piece['right'])
    
    if value == piece['left']:
        string = str(piece['right'])+","+str(piece['left'])

    return string

    
   
def showSolution(game):
    output = ''
    for  item in game:
        output += ' ' + str(item['value'])
    
    print output

def remove(pieces, piece):
    for index, p in enumerate(pieces):
        if p['id'] == piece['id']:
            pieces.pop(index)
            break
    return

def match(p1, value):
    if p1['left'] == value or p1['right'] == value:
        return True
    return False

def solution(pieces, piece, valor):
    found = False
    i = 0
    while i < len(pieces):
        current = pieces[i]
        print "Current:" + str(current)
        
        if match(current, valor):
            auxPiece = current
            if current['left'] == valor:
                auxValue = current['right']
            else:
                auxValue = current['left']
            found = True
            break
        i += 1
    
    if found:
        if len(pieces) == 1:
            return showPiece(piece, valor) + "|" + showPiece(auxPiece, auxValue)
        else:
            copy_copy = copy.deepcopy(pieces)
            remove(copy_copy, auxPiece)
            
            result = solution(copy_copy, auxPiece, auxValue)

            if len(result) == 0:
                return ""
            else:
                return showPiece(piece, valor) + "|" + result
    return "" 
    


if __name__== "__main__":

    pieces = [
        {
            'id': 1,
            'left': 3,
            'right': 4,
        },
        {
            'id': 2,
            'left': 2,
            'right': 5,
        },
        {
            'id': 3,
            'left': 3,
            'right': 6,
        },
        {
            'id': 4,
            'left': 4,
            'right': 5,
        },
        {
            'id': 5,
            'left': 3,
            'right': 2,
        },
        {
            'id': 6,
            'left': 5,
            'right': 1,
        },
        {
            'id': 7,
            'left': 6,
            'right': 2,
        }
    ]

    for piece in pieces:
        copy_pieces = copy.deepcopy(pieces)
        remove(copy_pieces, piece)
        result = solution(copy_pieces, piece, piece['right'])

        if len(result) > 0:
            break
        else:
            result = solution(copy_pieces, piece, piece['left'])
            if len(result) > 0:
                break
    
    if len(result) == 0:
        print "Sem solucao"
    else:
        print result
    




