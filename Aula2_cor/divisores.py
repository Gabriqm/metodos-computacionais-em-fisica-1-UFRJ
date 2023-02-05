'''
Sem erros.
Observação: Poderia ter sido impressa alguma mensagem junto ao comando 'input()'
ou anteriormente em um comando 'print()' para que o usuário fosse alertado da
necessidade de se inserir um número.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = (int(input()))     #Aqui colocamos a variável "n" para o usuário escolher o valor desejado.
i = n                  #Aqui coloquei a variável "i" como uma variável auxiliar para que seja possível rodar a condição mais abaixo
divisores = 0          #Aqui criei a variável "divisores" para assim que o "if" abaixo for rodando, será feita a soma com ele.
(print ("Divisores:"))  #Aqui coloquei a string para identificar que são os divisores
while i != 0:          #Coloquei o loop para quando "i" for diferente de 0.
    if n%i == 0:          #Nessa condição, quando o resto da divisão de "n" por "i" for 0, "i" será impresso pois será um divisor de "n"
       print (i)
       divisores = divisores + 1 #Criei essa variável para fazer a contagem dos divisores para que no final seja demonstrada a quantidade deles, ela roda sempre que a condição dada acima for "True".
    i -= 1
print ("total = ", divisores) #Aqui utilizei a função print para explicitar a variável "divisores" acima.


# In[ ]:





# In[ ]:




