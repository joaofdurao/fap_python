# Faça um Programa que peça a temperatura em
# graus Fahrenheit,
# transforme e mostre a temperatura em graus
# Celsius.
# C = 5 * ((F-32) / 9).

def converte_temp(tmp_faren):
    return 5 * ((tmp_faren-32) / 9)

faren = float(input('Digite o valor da temperatura em farenheit: '))

celsius = converte_temp(faren)

print(f'A temperatura equivalente em Celsius é: {celsius:.2f}')