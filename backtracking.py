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
    piece = list(reversed(piece))

    return piece

# tenta encaixar peca no head do jogo
def match(piece, game):
    if len(game) == 0:
        return True
    
    return game[-1][1] == piece[0]
        

def backtracking(pieces, game, n):

    # talvez nao precise desse if
    # if n == len(game):
    #     return game
    
    for index, piece in enumerate(pieces):
        
        # copias sao feitas para a chamada recursiva nao alterar os valores
        # qndo voltar da recursao sempre tem o estado em que estava
        if match(piece, game):
            game.append(piece)
            
            restOfPieces = copy.copy(pieces)
            restOfPieces.pop(index)

            newGame = copy.copy(game)
            
            result = backtracking(restOfPieces, newGame, n)           

            if n == len(result):
                return result
            
            # volta o jogo retirando ultima peca adicionada
            piece = game.pop(-1)                        

        piece = flip(piece)

        # faz a mesma coisa que o if acima, porem tentando com a peca virada
        if match(piece, game):
            game.append(piece)
            
            restOfPieces = copy.copy(pieces)
            restOfPieces.pop(index)

            newGame = copy.copy(game)

            result = backtracking(restOfPieces, newGame, n)

            if n == len(result):
                return result
            
            piece = game.pop(-1)

        piece = flip(piece)
    
    return game
        
    

if __name__== "__main__":
    
    pieces = [ [4, 6], [5, 4], [4, 4], [6, 6], [6, 6], [5, 0] ] 
    n = 6
    
    game = []

    result = backtracking(pieces, game, n)

    if len(result) != n:
        print "Sem solucao!"
    else:
        print result
        
       
    
    




