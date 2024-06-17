from statistics import mean


notas = [0,0,0,0]

for i in range(4):
    notas[i] = float(input(f'Digite sua {i + 1}ª nota: '))

print(f'A sua média foi: {mean(notas)} ')