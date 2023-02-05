'''
Gabriella
  - sem erros
  obs: Não indica o valor inicial de x
'''
#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
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


def dg(x):                     #defini a derivada da função acima após calcular à mão
    d = -np.exp(-x) - np.cos((np.pi*x)/2)*(np.pi/2)
    return d
xi = 0.            
limite = 100
acc = 1*(10**-7)
nit = 0
delta = 10**7
while abs(delta) > acc and nit < limite:      #coloquei o método de Newton Raphson para calcular a raiz
    x = xi - (g(xi)/dg(xi))
    delta = x-xi
    xi = x
    nit = nit + 1
print ("Número de iterações:", nit)
print ("A Raiz é:", xi)





