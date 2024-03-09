# defina a equação f(x) que você quer resolver
def f(x):
    return x**4 - 26*(x**2) + 24*x+21

# calcula a raiz da equação f(x) usando o método da falsa posição


def falsa_posicao(a, b, tol, max_iter):
    print(f"Resultado de f(a) = {f(a)}")
    print(f"Resultado de f(b) = {f(b)}")
    if f(a) * f(b) >= 0:
        print("O método da falsa posição não é aplicável neste intervalo.")
        return None

    if f(a) > 0:
        print(
            f" I | {'+a':^10} | {'f(a)':^10} | {'-b':^10} | {'f(b)':^10} | {'Xn':^10} | {'f(Xn)':^10} |")
    else:
        print(
            f" I | {'-a':^10} | {'f(a)':^10} | {'+b':^10} | {'f(b)':^10} | {'Xn':^10} | {'f(Xn)':^10} |")
    i = 0
    while i < max_iter:
        i += 1

        # Cálculo do ponto intermediário usando a fórmula da falsa posição
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(
            f" {i} | {a:^10.4f} | {f(a):^10.6f} | {b:^10.6f} | {f(b):^10.6f} | {c:^10.6f} | {f(c):^10.6f} |")

        # Verifica se c é a raiz ou se a tolerância foi atingida
        if abs(f(c)) < tol:
            print(f"\nRaiz encontrada: {c} após {i} iterações.")
            return c

        # Atualiza o intervalo apropriado para a próxima iteração
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print(f"Não foi possível encontrar a raiz após {max_iter} iterações.")
    return None


# Defina o intervalo [a, b], a tolerância e o número máximo de iterações
a = 1
b = 2
tolerance = 0.01
max_iterations = 100

# Chama a função falsa_posicao
falsa_posicao(a, b, tolerance, max_iterations)
