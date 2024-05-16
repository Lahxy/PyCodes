frase_inicial=input('Digite a palavra ou frase para análise, sem assentos: ')
frase=frase_inicial.upper()
frase=frase.replace(' ', '')
frase=frase.replace(',', '')
frase=frase.replace('.', '')
frase=frase.replace('-', '')
frase_invertida=frase[::-1]
print('Ordem normal: ',frase)
print('Ordem invertida: ',frase_invertida)
if frase==frase_invertida:
	print(f'>>{frase_inicial}<< é um palíndromo')
else:
	print(f'>>{frase_inicial}<< não é um palíndromo')