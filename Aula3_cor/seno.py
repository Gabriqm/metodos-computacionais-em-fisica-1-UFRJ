'''
Gabriella
 - sem erros
OBS: indicar no print por qual método está sendo calculado o seno
Obs: por que usar dois valores diferentes de x, um para a serie e outro para o da biblioteca matematica? A comparacao tem que ser com o mesmo.

'''
#!/usr/bin/env python
# coding: utf-8


from math import *      #importar a biblioteca "Mathematica".
x = float(input("Coloque o ângulo "))   #Definir a variável que será o ângulo para calcular o seno.
n = int(input("Coloque o valor de n ")) #Definir a variável que será a quantidade de elementos.
sen = 0  #Definir a variável inicial do seno que mais tarde será definida em uma fórmula.
for n in range(0,n+1):   #Abrir um loop for para que o n vá do zero até o valor que estipularmos.
    sen +=(-1)**n/(factorial(2*n + 1))*x**(2*n+1)
print ("o resultado é ",sen)  




#O código abaixo é para fazer a comparação solicitada
u = float(input("insira o ângulo "))
y = sin(u)
print ("o resultado é ",y)





