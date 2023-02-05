'''
 - Sem erros
OBS: Faltaram legendas no gráfico

'''
import numpy as np
import matplotlib.pyplot as plt

def dxdt(x,t):        #defini a função derivada.
    '''Função que retorna a derivada solicitada'''
    dx = x**2 + 1
    return dx
def Euler(f,xi,ti,tf,n):    #defini a função que usa o método de Euler.
    '''Resolve a EDO de primeira ordem pelo método de Euler'''
    t=np.zeros(n+1)
    x=np.zeros(n+1)
    ti=t[0]
    xi=x[0]
    h=(tf-ti)/n
    for s in range(n-1):
        t[s+1]=t[s] + h
        x[s+1]=x[s] + h*dxdt(x[s],t[s])
    return x,t
ti=0
tf=1
xi=0
n=5

x,t = Euler(dxdt,xi,ti,tf,n)   #defini as variáveis que a função de Euler me retorna.

plt.plot(t,x,"r.",t,np.tan(t),"b*")     #plotei o gráfico solicitado.
plt.xlabel('t')
plt.ylabel('x')
plt.show()
