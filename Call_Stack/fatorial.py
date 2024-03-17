def fatorial(n):
    # Caso base: se n for 0 ou 1, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: calcular o fatorial de n - 1 e multiplicá-lo por n
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
numero = 5
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)
