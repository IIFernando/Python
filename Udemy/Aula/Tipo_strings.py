'''
Python é uma linguagem de programação
tipo de tipagem dinâmica e forte
str - string - texto
strings são textos que estão dentro de aspas
'''

a = 'Fernando'
b = 'Araujo'

# Aspas simples
print('Fernando Araujo')
print('Fernando "Araujo"')

# Aspas duplas
print("Fernando Araujo")

# Escape
print('Fernando \"Araujo\"')

# r
print(r'Fernando \"Araujo\"')


#Formatação F Strings
formatado = 'a={}, b={}'.format(a, b)
print(formatado)
