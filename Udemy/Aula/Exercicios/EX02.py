#Calculadora de IMC - Indice de massa corporea

peso = int(input('Informe seu peso: '))
altura = float(input('INforme sua altura: '))

imc = peso / altura ** 2

if imc > 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc:.2f} considerado, NORMAL')

elif imc > 25 and imc <= 29.9:
    print(f'Seu IMC é {imc:.2f} considerado, SOBREPESO')

elif imc > 30 and imc <= 34.9:
    print(f'Seu IMC é {imc:.2f} considerado, OBESIDADE GRAU I')

elif imc > 35 and imc <= 39.9:
    print(f'Seu IMC é {imc:.2f} considerado, OBESIDADE GRAU II')
    
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f} considerado, OBESIDADE GRAU III')