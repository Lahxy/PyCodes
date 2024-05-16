a=input('diga uma palavra e eu verificarei se é um palíndromo: ')
a=a.replace(' ' and '.' and ',' and '/' and '?' and '!' , '')
a=a.upper()
a_inv=a[::-1]
print(f'a ordem das letras é {a}')
print(f'a ordem invertida é {a_inv}')
if a==a_inv :
	print('eh um palíndromo')
else:
	print('não eh um palíndromo')