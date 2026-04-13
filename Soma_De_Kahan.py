def soma_de_kahan(numeros):
    soma = 0.0
    c = 0.0
    for x in numeros:
        y = x - c
        t = soma + y
        c = (t - soma) - y
        soma = t
    return soma