#!/usr/bin/python

import sys
import copy


result = []

def readFile():
    arq = open('entrada.txt', 'r')
    texto = arq.readlines()[1:]
    for linha in texto :
        piecesList.append(linha.rstrip('\n'))
    arq.close()

# flipa peca, se necessario
def flip(piece, value):
    if value == piece[0]:
        reversedPiece = copy.copy(piece)
        reversedPiece = list(reversed(piece))
        return reversedPiece
    
    return piece

def remove(pieces, piece):
    for index, p in enumerate(pieces):
        if p[1] == piece[1] and p[0] == piece[0]:
            pieces.pop(index)
            break
    return

# tenta encaixar value dos dois lados da p1
def hasMatch(p1, value):
    if p1[0] == value or p1[1] == value:
        return True
    return False


def backtracking(pieces, piece, borderPieceValue):
    found = False
    i = 0

    # dentre as pecas, procura um match
    while i < len(pieces):
        current = pieces[i]
        
        if hasMatch(current, borderPieceValue):

            # recebe lado esquerdo ou direito da peca que deu match para passar na recursao
            newBorderPieceValue = current[1] if current[0] == borderPieceValue else current[0]           

            found = True
            break
        i += 1
    
    if found:
        
        # caso base. adiciona a lista a peca da recursao cm a ultima peca da lista
        if len(pieces) == 1:
            result.append( flip(piece, borderPieceValue ))
            result.append( flip(current, newBorderPieceValue ))            
            return result

        else:
            
            # clona lista de pecas e remove a que tinha dado match
            piecesCloned = copy.deepcopy(pieces)
            remove(piecesCloned, current)
            
            backtracking(piecesCloned, current, newBorderPieceValue)

            if len(result) == 0:
                return []
            else:
                # piece eh a primeira peca
                result.insert(0, flip(piece, borderPieceValue))
                return result
    return []
    

if __name__== "__main__":

    pieces = [ [5, 5], [4, 6], [5, 4], [2, 6], [5, 0], [4, 4] ] 

  
    for piece in pieces:
        
        # clona lista de pecas e remove peca que sera enviada ao backtrackin
        piecesCloned = copy.deepcopy(pieces)
        remove(piecesCloned, piece)

        # lista sem item corrente, item corrente e lado direito do item corrente
        game = backtracking(piecesCloned, piece, piece[1])

        if len(game) > 0:
            break
        
        else:
            
            # lista sem item corrente, item corrente e lado esquerdo do item corrente
            game = backtracking(piecesCloned, piece, piece[0])
            if len(game) > 0:
                break
    
    if len(game) == 0:
        print "Sem solucao"
    else:
        print game
    




