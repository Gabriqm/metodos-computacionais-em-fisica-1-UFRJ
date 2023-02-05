'''
sem erros
'''

#!/usr/bin/env python
# coding: utf-8

def mysum(x):   #primeiro criei a função mysum
    """A função mysum(x) criada soma os elementos de uma lista"""   #expliquei o que ela faz
    y=x[0]        #criei um contador para o programa reconhecer os elementos
    for i in x[1:]:
        y += i
    return y
lista1=[1,2,3]     #defini as listas solicitadas)
lista2=[[1,2],[4,3]]
lista3=["Hello, ","World!"]

print(mysum(lista1)) #explicitei os resultados e a documentação
print(mysum(lista3))
print(mysum(lista2))
print(mysum.__doc__)
