import numpy as np

def learq() :

##    def extraiInt(s) :
##        if s == '0,00' :
##            return 0
##        else :
##            pi, pf = s.split(',')
##            return int(pi)
            
    try:
        arq = open("PROJETOS\ATIVIDADES\MegaSenaDezenasOrdemCrescente2.csv", encoding="utf8") 
    except:
        print("A abertura do arquivo falhou!")
        quit()
    s = arq.read()
    arq.close()
    cont = 0   # conta o número de linhas totais, incluindo título (texto) e última linha (vazia)
    for s1 in s.split('\n'):
        cont = cont + 1    
    n = cont - 2
    matrizMega = np.empty((n, 10), dtype=int)
    cont = -1
    for s1 in s.split('\n'):
        if cont > -1  : # exclui a primeira linha (texto)
            if s1 != '' : # exclui eventuais linhas em branco (incluindo a última)
                Conc,Data,D1,D2,D3,D4,D5,D6 = s1.split(',')
                dia,mes,ano = Data.split('/')
                matrizMega[cont] = [Conc,dia,mes,ano,D1,D2,D3,D4,D5,D6]
                cont = cont + 1
        else :
            cont = cont + 1      
    return matrizMega, n

    
