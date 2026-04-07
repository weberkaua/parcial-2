# Solicita os valores de C, I e T
C = float(input("Digite o valor do capital (C): "))
I = float(input("Digite a taxa de juros (I) em %: "))
T = float(input("Digite o tempo (T) em períodos: "))

# Calcula o valor dos juros (J) utilizando a fórmula
J = (C * I * T) / 100

# Exibe o resultado
print(f"O valor dos juros (J) é: {J:.2f}")

