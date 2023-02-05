'''
[linha  51 e 55] 'if' e 'else' desnecessários.
[linhas 44 e 64] Precisa adicionar 1 ao k final pois o último a ser
comparado foi o k[i+1]
[linha 57 e 69] Precisa adicionar 1 ao k final pois o último a ser
comparado foi o k[u+1]
Obs: o valor de k encontrado para a integral de 'np.exp(-y**2/2)'
(multiplicado por 1/np.sqrt(2*np.pi) ao final) é diferente do valor
de k encontrado para a integral de '1/np.sqrt(2*np.pi)*np.exp(-y**2/2)'

'''
#!/usr/bin/env python
# coding: utf-8

from math import *
import numpy as np

def e(y):                      #Defini a equação que será integrada
    ex = np.exp(-y**2/2)
    return ex

def trapezio(e,a,b,k):         #Defini a função trapézio
    deltaxk = (b-a)/2**k
    j = 1
    soma = 0
    while j <= (2**k-1):
        fj = e(a + j*deltaxk)
        soma += fj
        j += 1
    tk = deltaxk/2 * (e(a)+2*soma+e(b))
    return tk
    
def simpson(tk,tk1):             #Defini a função Simpson, sendo tk = tk - 1 e tk1 = tk
    sk = tk1 + (tk1 - tk)/3
    return sk    

a = -2
b = 2
precisao = 10**-6
k=np.array(range(0,21,1))

u=0                          #fazendo a convergência para o método do trapézio para encontrar o k ideal
for u in k:
    if abs(trapezio(e,a,b,k[u+1])-trapezio(e,a,b,k[u])) < precisao:
        break
    else:
        u+=1

i=0                  #fazendo a convergência para o método de simpson para encontrar o k ideal
for i in k:
    if i==0:
        tk = trapezio(e,a,b,k[i])
        tk1 = trapezio(e,a,b,k[i+1])
        sk1 = simpson(tk,tk1)            
    else:
        tk = trapezio (e,a,b,k[i])
        tk1 = trapezio(e,a,b,k[i+1])
        sk2 = simpson (tk,tk1)
        if abs(sk2 - sk1) < precisao:
            break
        sk1=sk2
        
intTrapezio = 1/np.sqrt(2*np.pi)*trapezio(e,a,b,u)
print("A integral calculada pelo método do trapézio é %.5f por k = %d" %(intTrapezio,u))



metSimpson = (1/np.sqrt(2*np.pi))*simpson(tk,tk1)
print("A integral calculada pelo método de Simpson é %.5f por k = %d" %(metSimpson,i))

#Poderíamos otimizar o tempo calculando a integral definida de [0,2] e multiplicando-a por 2, pois assim as áreas seriam menores e seriam usados menos "k", otimizando o processamento do programa.
