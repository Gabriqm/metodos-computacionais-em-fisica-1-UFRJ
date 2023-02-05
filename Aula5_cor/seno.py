'''
[linha 16]- O range deveria ser até N, pois a série começa a ser contada no zero,
do modo que está escrito contamos um termo a mais.
Em consequencia o gráfico está diferente de como está escrito na legenda.
5/6
'''
#!/usr/bin/env python
# coding: utf-8

from math import *
import numpy as np
import matplotlib.pyplot as plt
def taylor_seno(x,n):
    sen = 0
    for n in range(0,n+1):
        sen +=((-1)**n)/(factorial(2*n + 1))*(x**(2*n+1))
    return sen

x = float(input("Coloque o ângulo: "))   #Definir a variável que será o ângulo para calcular o seno.
n = int(input("Coloque o valor de n: ")) #Definir a variável que será a quantidade de elementos.

print("valor obtido pela Série de Taylor criada:", taylor_seno(x,n))
print("valor da biblioteca math:", sin(x))
print("diferença entre a Série de Taylor e a biblioteca:", taylor_seno(x,n) - sin(x))     #Demonstrei os valores das diferenças para comparar com os do termo de próxima ordem
termoSeg = taylor_seno(x,n+1) - taylor_seno(x,n)
print("o termo de próxima ordem é: ",termoSeg)


x_ = np.linspace(0, 3*np.pi/2, 51)    #aqui coloquei os gráficos que foram solicitados no intervalo definido na variável "x_"
y = np.sin(x_)
y1=taylor_seno(x_,1)
y2=taylor_seno(x_,2)
y3=taylor_seno(x_,3)
y4=taylor_seno(x_,4)
y5=taylor_seno(x_,5)
x_grau=x_*180/np.pi                  #converti de radiano para graus e em seguida plotei os gráficos, identificando cada um
plt.plot(x_grau,y, label="sen(x)")
plt.plot(x_grau,y1, label="n=1")
plt.plot(x_grau,y2, label="n=2")
plt.plot(x_grau,y3, label="n=3")
plt.plot(x_grau,y4, label="n=4")
plt.plot(x_grau,y5, label="n=5")
plt.ylabel("Sen(x)")              #aqui apenas ajeitei o gráfico para melhor compreensão
plt.xlabel("Ângulo")
plt.grid(True)
plt.ylim(-2,2)
plt.title("Série de Taylor-sen(x)")
plt.legend()
plt.show()
