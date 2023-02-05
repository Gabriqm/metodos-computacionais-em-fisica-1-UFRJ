'''
O programa roda mas não fornece o resultado esperado quando não temos uma raiz entre os intervalos
Erro: Na linha 33 foi escrito sys.exit e não sys.exit()
Obs 1: poderia ter printado em tela o motivo pelo qual o programa não pode encontrar raiz quando g(xmin)*g(xmax)>0
Obs 2: A questão exigia a utilização de uma precisão relativa (|x_n-x_{n-1}|/x_n) de 1.e-7
'''

#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import sys
def g(x):                   #defini a equação a ser utilizada
    f=(np.exp(-x) - np.sin((np.pi*x)/2))
    return f
x=np.linspace(0,4)         #defini um intervalo de variáveis e abaixo embelezei o gráfico para ficar mais apresentável
y=g(x)
plt.grid(True)
plt.title("Gráfico da função g(x)")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.plot(x,y)
plt.show()



xmin=0.3                    #os valores máximo e mínimo observei no gráfico plotado acima
xmax=0.5
lim = 100
acc = 1*(10**-7)
if g(xmin)*g(xmax)>0:                        #coloquei as condições solicitadas 
    sys.exit
nit = 0
while abs(xmax - xmin) > acc and nit < lim:    #construí o método da bisseção para encontrar a raiz
    xmed = (xmin+xmax)/2
    fmed = g(xmed)
    if g(xmin)*g(xmed)<0:
        xmax = xmed
    else:
        xmin=xmed
    nit = nit+1
print ("Número de iterações:", nit)
print ("A raiz é:", xmed)
    
    


# In[ ]:




