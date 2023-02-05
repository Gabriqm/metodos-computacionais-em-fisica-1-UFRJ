'''
O programa roda e fornece os resultados esperados.
Obs: O aluno não inseriu label nos eixos.
'''
#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
gravidade=np.loadtxt("gravidade.dat")       #importei a lista fornecida e calculei a quantidade de elementos e as média.
quantidade = len(gravidade) 
media = sum(gravidade)/len(gravidade)
x=0
for u in gravidade:                         #aqui coloquei um contador "u" para passar pela lista fornecida e alterar a variável "x"
    x+=(u - media)**2
desvioPadrao = ((1/(quantidade - 1))*x)**(1/2)  #montei a variável com a equação fornecida para o desvio padrão.
print("A média dos valores é:","%.3f" %(media))
print("O Desvio Padrão dos dados fornecidos é:","%.3f" % (desvioPadrao))
print("Os dados das gravidades são:", gravidade)
plt.hist(gravidade, bins=20,edgecolor="k")  #plotei dois histogramas com as quantidades propostas de bins, inseri bordas e limites em x e y, além de um título e grade.
plt.hist(gravidade, bins=60,edgecolor="k")
plt.xlim(975,996)
plt.ylim(0, 850)
plt.grid(True)
plt.title("Histograma das gravidades")
plt.show()






