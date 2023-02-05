'''
O programa roda e fornece os reusltados esperados.
Obs 1: Programa sem comentários
Obs 2:  Cuidado com divisões por zero. Caso o valor do chute inicial seja 0 ou 1.5e11 teriamos uma divisão por zero
na função e sua derivada.
Obs 3: Cuidado com chutes iniciais excessivamente longe do valor da raiz. Isso pode gerar lentidão desnecessária no programa.
Observe o gráfico da função para decidir um chute inicial.
'''

def lg(x):
    l=(G*M)/x**2 - (G*m)/(R-x)**2 - (omega**2)*x
    return l
def dlg(x):
    dl= -G*2*M/x**3 - G*2*m/(R-x)**3 - omega**2
    return dl

G=6.674*10**(-11)
M=1.989*10**(30)
m=5.9736*10**(24)
R=1.5*10**(11)
omega=1.992*10**(-7)

xi = 0.5
lim = 100
acc = 10**(-7)
nit = 0
delta = 10**(7)
while abs(delta)>acc and nit<lim:
    x=xi - (lg(xi)/dlg(xi))
    delta = x-xi
    xi = x
    nit = nit + 1
print ("Numero de iterações:", nit)
print ("r =", x)
