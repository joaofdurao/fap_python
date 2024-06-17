# Uma nutricionista identificou que seus pacientes não estavam consumindo água em quantidade 
# adequada conforme seu peso. Como solução, ela requisitou a um programador o desenvolvimento 
# de um programa. Esse programa precisa conter as seguintes informações dos pacientes: nome, 
# número do WhatsApp, peso e altura. Posteriormente, o programa deve calcular e apresentar o 
# consumo diário recomendado de água para cada paciente com base em seu peso. O programa também 
# deve calcular IMC, seguindo as regras abaixo:

# IMC abaixo de 18.5: Abaixo do peso, 
# IMC entre 18.5 e 24.9: Peso normal, 
# IMC entre 25 e 29.9: Sobrepeso, 
# IMC entre 30 e 34.9: Obesidade grau 1 (leve), 
# IMC entre 35 e 39.9: Obesidade grau 2 (moderada) e 
# IMC acima de 40: Obesidade grau 3 (mórbida).

# Jovens até os 17 anos	40 ml por cada kg
# De 18 a 55 anos	35 ml por cada kg
# De 55 a 65 anos	30 ml por cada kg
# 66 anos em diante	25 ml por cada kg

# Em seguida exibir os resultados.

# Exemplo:
# Nome: Paulo - Whatsapp - 9 88776655, Peso: 90 - Altura: 1.7 - Consumo de água diário:  2.8 litros - IMC: 25 - Nível de obesidade: .Sobrepeso.


def calcula_imc(peso, altura):
    imc = peso/(altura*altura)

    if imc < 18.5:
        nivel = 'Abaixo do Pesso'
    elif imc <= 24.9:
        nivel = 'Peso normal'
    elif imc <= 29.9:
        nivel = 'Sobrepeso'
    elif imc <= 34.9:
        nivel = 'Obesidade grau 1 (leve)'
    elif imc <= 39.9:
        nivel = 'Obesidade grau 2 (moderada)'
    elif imc > 40: 
        nivel = 'Obesidade grau 3 (mórbida)'

    return imc, nivel

def calcula_agua(peso, idade):
    if idade <= 17:
        consumo_agua_ml = 40 * peso
    elif idade <= 55:
        consumo_agua_ml = 35 * peso
    elif idade <= 65:
        consumo_agua_ml = 30 * peso
    elif idade >= 66:
        consumo_agua_ml = 25 * peso

    consumo_agua = consumo_agua_ml/1000

    return consumo_agua

def print_paciente(paciente_dict):
    print(f"Nome: {paciente_dict['Nome']} - Idade - {paciente_dict['Idade']} - Whatsapp - {paciente_dict['WhatsApp']}, Peso: {paciente_dict['Peso']} - Altura: {paciente_dict['Altura']} - Consumo de água diário:  { paciente_dict['Consumo_de_agua']:.2f} litros - IMC: {paciente_dict['IMC']:.2f} - Nível de obesidade: {paciente['Nivel']}.")

paciente = {
    'Nome': '',
    'Idade': 0,
    'WhatsApp': '',
    'Peso': 0.0,
    'Altura': 0.0,
    'Consumo_de_agua': 0.0,
    'IMC': 0.0,
    'Nivel': ''
}

print('-------------------- Calculadora FIT --------------------')
paciente['Nome'] = input('Digite seu nome: ')
paciente['Idade'] = int(input('Digite sua idade: '))
paciente['WhatsApp'] = input('Digite seu WhatsApp: ')
paciente['Peso'] = float(input('Digite seu Peso em quilos: '))
paciente['Altura'] = float(input('Digite seu Altura em metros: '))
print('---------------------------------------------------------')

paciente['IMC'], paciente['Nivel'] = calcula_imc(paciente['Peso'], paciente['Altura'])
paciente['Consumo_de_agua'] = calcula_agua(paciente['Peso'], paciente['Idade'])

print_paciente(paciente)