adicao = 10 + 10
print(f'Adição {adicao}')

subtracao = 10 - 10
print(f'Subtração {subtracao}')

multiplicacao = 10 * 10
print(f'Multiplicação {multiplicacao}')

divisao = 10 / 10 # Sempre retorna um float
print(f'Divisão {divisao}')

divisao_int = 10 // 10
print(f'Divisão inteira {divisao_int}')

exponenciacao = 2 ** 10
print(f'Exponenciação {exponenciacao}')

modulo = 55 % 2 #Resto da divisão
print(f'Módulo {modulo}')

#Ordem de prescedencia, tudo que estiver entre () é executado primeiro.
conta = (1 + int(0.5 + 0.5) ** 5 + 5)
print(conta)