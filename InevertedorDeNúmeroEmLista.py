lista= input('insira numeros: ').split()
print(f'\na lista é {lista}\n')
n=1
for i in lista:
	print(f'{n}-{i[::-1]}')
	n=n+1