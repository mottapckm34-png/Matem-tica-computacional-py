
def f(x):
    return x**2 - x - 2

def g(x):
    return x**2 - 2

def dg(x):
    return 2*x 
def df(x):
    return 2*x - 1

x0 = 1.5
tolx = 1e-5
toly = 1e-5
cont = 0
x1 = 0.0

if abs(dg(x0)) >= 1:
        print("O método não é convergente para esta função.\n")
else:
    while (abs(x1 - x0 ) >= tolx):
        x1 = g(x0)
        x0 = x1
        cont += 1
        if (cont > 100):
            break
if abs(f(x1)) < toly:
    print("O método convergiu para a raiz: ", x1, "\n")
else:
    print("O método não convergiu para uma raiz dentro do número máximo de iterações.\n")    







































