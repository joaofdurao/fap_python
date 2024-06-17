# Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido
# mês.

def calcula_salario( salario, horas):
    return salario * horas

salario = float(input('Quanto voce ganha por horas? '))
horas = float(input('Digite suas horas tabalhadas por mês: '))

salario_mes = calcula_salario(salario, horas)

print('Seu salario mensal é R$ ', salario_mes)