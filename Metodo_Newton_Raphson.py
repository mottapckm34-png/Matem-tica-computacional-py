def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x0 = 1.5
tol= 1e-5
x1 = 0.0
cont = 0
numero_iteracoes = 0

while True:

    if df(x0) == 0:
        print("Derivada é zero. O método de Newton-Raphson falhou.")
        break
    x1 = x0 - f(x0)/df(x0)
 
    cont += 1
    numero_iteracoes += 1
    x0 = x1
    if cont > 100:
        print("Número máximo de iterações atingido. O método de Newton-Raphson falhou.")
        break

    if abs(f(x1)) < tol:
        print("O método de Newton-Raphson convergiu para a raiz: ", x1)
        break


print("Número de iterações: ", numero_iteracoes)

