def bisseccao(funcao, a, b, tol, max_iter):
    if funcao(a) * funcao(b) >= 0:
        print("A função deve ter sinais opostos em a e b.")
        return None
    g = 0.0
    fa = funcao(a)
    for i in range(max_iter):
        xm = (a + b) / 2  # Ponto médio
        g = funcao(xm)
        if g == 0 or (b - a) / 2 < tol:
            return xm  # Encontrou a raiz ou atingiu a tolerância

        if g * fa < 0:
            b = xm  # A raiz está entre a e xm
        else:
            a = xm  # A raiz está entre xm e b
            fa = g  # Atualiza fa para o próximo ciclo
    return (a + b) / 2  # Retorna o melhor palpite após max_iter iterações
