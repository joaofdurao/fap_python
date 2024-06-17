# Tendo como dado de entrada a altura (h) de uma
# pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
def define_genero(genero):
    if genero.lower() == 'masc':
        return 1
    elif genero.lower() == 'fem':
        return 0
    else:
        raise Exception('Genero não reconhecido')

def calcula_peso_by_altura(altura, genero):
    if genero == 1:
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7

altura = float(input('Digite sua altura atual: '))
gen = input('Digite MASC para masculino e FEM para feminino: ')
peso = calcula_peso_by_altura(altura, define_genero(gen))

print(f'Seu peso ideal, segundo sua altura é: {peso:.2f}')