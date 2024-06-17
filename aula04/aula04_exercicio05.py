# Tendo como dados de entrada a altura de uma
# pessoa, construa um algoritmo que calcule seu peso
# ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcula_peso_by_altura(altura):
    return (72.7 * altura) - 58

altura = float(input('Digite sua altura atual: '))
peso = calcula_peso_by_altura(altura)

print(f'Seu peso ideal, segundo sua altura é: {peso:.2f}')