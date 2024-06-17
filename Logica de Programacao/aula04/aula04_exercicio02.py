# Faça um Programa que converta metros para
# centímetros.

def convert(valor_metros):
    return valor_metros * 100

metros = float(input('Digite o valor em metros que deseja converter: '))
centimetros = convert(metros)
print(f'O valor em centímetros é igual a: {centimetros:.2f}')