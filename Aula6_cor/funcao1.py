'''
- Sem erros.
'''

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
plt.savefig("funcao1.pdf")      #usei a função para salvar em PDF, como solicitado
plt.show()
