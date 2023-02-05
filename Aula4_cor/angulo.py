'''
O programa roda mas não fornece resultados esperados para o caso de um ou dois vetores nulos e para os angulos de 0 e 180 graus.
Erro: O aluno não impôs uma condição que impede o cálculo do cosseno para o caso de um ou mais módulos serem nulos (divisão por zero).
Obs 1: Por tratar-se de uma variável float, os números no computador são aproximados. 
Portanto, para que seja possível calcularmos o valor exato do cosseno para ângulos paralelos, 
anti-paralelos e perpendiculares, devemos realizar arredondamentos utilizando a função round(), por exemplo. 
Obs 2: Não há necessidade de definir as variáveis in, jn e kn n=1,2 para utilizar os elementos de array de v1 e v2. Eles poderiam ser utilizados diretamente.
Além disso, recomenda-se utilizar as variáveis locais dentro de uma função para evitar troca de valores indesejadas em arrays do corpo principal.
'''
#!/usr/bin/env python
# coding: utf-8

from math import *  #importei a biblioteca Mathematica
import numpy as np   #importei a biblioteca Numpy
def angulo(x,y):     #defini a função "angulo" abaixo utilizando a fórmula do produto escalar.
    """A função entrega o valor do ângulo em radiano entre dois vetores até três dimensões."""  #documentação da função
    i1 = float(v1[0])  #defini variáveis para utilizar na equação como as componentes dos vetores.
    i2 = float(v2[0])
    j1 = float(v1[1])
    j2 = float(v2[1])
    k1 = float(v1[2])
    k2 = float(v2[2])
    t = (np.dot(v1,v2))/((sqrt((i1)**2 + (j1)**2 + (k1)**2))*(sqrt((i2)**2 + (j2)**2 + (k2)**2))) #passei a fórmula do produto escalar em linguagem do python
    theta = acos(t) #o ângulo é o arco cosseno do valor fornecido pela variável "t" acima
    return theta
v1 = np.array([1,1,1])   #criei uma lista e converti em array para conseguir utilizar os elementos na equação
v2 = np.array([-1,-1,-1])
u = angulo(v1,v2)  #a variável que defini para mostrar o ângulo
print("O ângulo(em radiano) entre os vetores v1 e v2 é: %.4f" %u) #O valor do ângulo em radiano
print(angulo.__doc__)  #a documentação da função criada






