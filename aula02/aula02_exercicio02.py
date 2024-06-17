"""Elabore um algoritmo que receba o nome do estudante, 
a primeira e a segunda nota da avaliação. 
Ao final exiba o nome, a primeira nota,
a segunda nota e a média do estudante."""

from statistics import mean

nome_estudante = input('Digite seu nome: ')
notas = []
notas.append(float(input('Digite a primeira nota: ')))
notas.append(float(input('Digite a segunda nota: ')))

print(f'Aluno: {nome_estudante}\nNota 1: {notas[0]}\nNota2: {notas[1]}\nMedia: {mean(notas)}')