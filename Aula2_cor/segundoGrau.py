'''
Viviane
O programa roda mas não fornece os resultados esperados para nenhuma das raizes.
Erro 1: Em nenhum dos 3 casos ele colocou parênteses no denominador para calcular as raizes (linhas 37, 38, 48, 57, 58). 
Obs 1: Ele printa delta mas não diz que é delta.
Obs 2: Não se deve comparar uma variável float usando == pois os números no computador são aproximados. Deve-se usar if fabs(delta)<1.e-12  (ou qualquer numero muito pequeno)
Obs 3: Poderia ter limitado as casas decimais em algumas respostas (linha 40, 41, 50, 60, 61) 
4.0
'''

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import *                             #Aqui foi importada a biblioteca Mathematica para que fosse possível usar algumas funções.
a=float(input("Digite o valor de a "))         #Coloquei uma variável aonde o usuário será solicitado inserir um valor para fazer a equação.
while a == 0:                                  #Aqui inseri um loop para a variável "a" ser diferente de 0, senão não seria uma equação de segundo grau.
    print("Essa variável precisa ser diferente de zero")
    a=float(input("Digite o valor de a "))
b=float(input("Digite o valor de b "))        # As variáveis "b" e "c" seguem o mesmo padrão da "a", para que o usuário consiga definir valores.
c=float(input("Digite o valor de c "))
delta = b**2 - 4*a*c            # Aqui determinei a variável delta que é essencial na elaboração das condições para determinação das raízes


# In[2]:


print (delta)     # Utilizei a função "print" para mostrar o valor da variável "delta"


# In[3]:


if delta > 0:                      # Essa é a primeira condição para o caso em que "delta" seja maior que zero, assim possibilitando duas raízes reais.
    x1 = (-b + sqrt(delta))/2*a
    x2 = (-b - sqrt(delta))/2*a
    print ("Existem duas soluções reais")
    print (x1)
    print (x2)


# In[7]:


if delta == 0:         # Nessa segunda condição temos o caso em que delta seja igual a 0, tanto que utilizei a operação "==" para determinar era "True" ou "False"
    x = (-b/2*a)
    print ("Existe uma solução real")
    print(x)


# In[9]:


if delta < 0:                     # Nessa última condição, temos o caso aonde delta é menor que 0, o que nos leva a duas raízes complexas
    x1 = (-b + (delta)**(1/2))/2*a
    x2 = (-b - (delta)**(1/2))/2*a
    print ("Existem duas soluções imaginárias")
    print (x1.real, '+', x1.imag,'i')
    print (x2.real, '+', x2.imag,'i')


# In[ ]:




