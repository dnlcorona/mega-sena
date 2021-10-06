# -*- coding: utf-8 -*-
import numpy as np
import auxiliar as aux

def q1():
                  
    print('Este programa exibe as informações de um concurso e \nverifica se um jogo de 6 dezenas já foi sorteado na Megasena')
    Mega, numConcursos = aux.learq()
    print('\nO arquivo lido possui resultados de %d concursos!' %numConcursos)
    print('O primeiro sorteio registrado foi em %d/%d/%d.' %(Mega[0][1], Mega[0][2], Mega[0][3]))
    print('O último sorteio registrado foi em %d/%d/%d.' %(Mega[numConcursos-1][1], Mega[numConcursos-1][2], Mega[numConcursos-1][3]))
    print()

    while True:
        opcao = int(input('\nEntre com o número do concurso (ou 0 para terminar): '))
        if opcao >= 1 and opcao <= 2415:
            linhaAtual = 0
            linhaAtual = opcao-1
            print(f'Concurso: {opcao}. Data do sorteio: {Mega[linhaAtual][1]}/{Mega[linhaAtual][2]}/{Mega[linhaAtual][3]}.')
            print(f'Dezenas sorteadas: {Mega[linhaAtual][4]}, {Mega[linhaAtual][5]}, {Mega[linhaAtual][6]}, {Mega[linhaAtual][7]}, {Mega[linhaAtual][8]} e {Mega[linhaAtual][9]}.')
        elif opcao == 0:
            print("Veja se o seu palpite já foi sorteado alguma vez!\nForneça 6 números diferentes entre 1 e 60")
            d1 = int(input("Dezena 1: "))
            if d1 >=1 and d1 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")
            d2 = int(input("Dezena 2: "))
            if d2 >=1 and d2 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")
            d3 = int(input("Dezena 3: "))
            if d3 >=1 and d3 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")
            d4 = int(input("Dezena 4: "))
            if d4 >=1 and d4 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")
            d5 = int(input("Dezena 5: "))
            if d5 >=1 and d5 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")
            d6 = int(input("Dezena 6: "))
            if d6 >=1 and d6 <=60:
                pass
            else:  
                print("Valor inválido! A dezena deve estar entre 1 e 60")      
        else:
            print("Concurso inexistente! valor deve estar entre 1 e 2415")

'''  
for x in range(len(Mega)):  
    for y in range(len(Mega[x])):
        if Mega[x][y] == opcao:
        print(f'{Mega[x][y]}')
'''
q1()