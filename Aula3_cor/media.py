#!/usr/bin/env python
# coding: utf-8
'''
- Sem erros.

OBS: Poderia ter feito uma breve introdução sobre do que se trata o programa
OBS: Escolher melhor os nomes das variáveis a serem utilizadas. Os nomes "x", "b" e "c" não são
grandes indicativos da real finalididade das variáveis.
'''

from math import *               #Primeiramente importei a biblioteca Math para garantir o possível uso de funções.
import numpy as np               #Agora importo a biblioteca numpy para conseguir importar o arquivo de texto dentre outras funções.
a=np.loadtxt("media.txt")        #Importo o arquivo txt para o programa e uso a função "print" para ver se está corretamente importada.
print(a)


numeroAlunos = len(a)            #Utilizei a função "len" para explicitar a quantidade de alunos baseada na lista
print ("O número total de alunos é:",numeroAlunos)


media = sum(a)/len(a)            #Utilizei a função "sum" e dividi pela "len" para obter a média desejada em uma variável.
print("A média é:",media)


x = 0            #Criei uma variável para servir da metade Soma da equação de desvio padrão dada.
for u in a:       # Denominei de "u" a variável que serve de contador para a lista do Array.
    x += (u - media)**2         #Conforme essa condição for passando, o "u" será alterado nessa variável".
desvioPadrao = sqrt(((1/(numeroAlunos - 1))*x))         #Montei a fórmula final para calcular o desvio padrão.
print("O desvio padrão calculado pela fórmula pedida é:","%.1f" %(desvioPadrao))

print("Comparação com a função de desvio padrão do Numpy:",np.std(a)) 
    
print("Comparação com a função de média do Numpy:", np.mean(a))

b = 0    #Para calcular quem foi aprovado e reprovou, utilizei de duas variáveis auxiliares para servirem de contadores.
for u in a:
    if u>=7:
        b += 1
print ("A quantidade de aprovados é:",b)

c = 0
for u in a:
    if u < 3:
     c += 1
print ("a quantidade de reprovados é:",c)


