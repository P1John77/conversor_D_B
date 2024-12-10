
def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"

    restos = []

    while decimal > 0:
        resto = decimal % 2
        restos.append(resto)
        decimal //= 2

    restos.reverse()

    binario = ''.join(map(str, restos))
    return binario

numero_decimal = int(input("Digite um valor decimal: "))

resultado_binario = decimal_para_binario(numero_decimal)
print(f"O número decimal {numero_decimal} convertido em binário é: {resultado_binario}")
