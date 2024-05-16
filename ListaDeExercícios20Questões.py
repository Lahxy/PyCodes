#1. Escreva um programa que imprima "Olá, mundo!" na tela.

print ('Olá, mundo')

#2. Crie uma variável chamada nome e atribua a ela o seu nome. Em seguida, imprima "Olá," seguido do valor dessa variável.

nome='João Victor Pinheiro Reis'
print(f'Olá, {nome}')

#3. Escreva um programa que calcule a soma de dois números e imprima o resultado.

a=float(input('diga o primeiro número: '))
b=float(input('diga o segundo número: '))
print(f'A soma desses números é {a+b}')

#4. Crie uma lista com cinco números inteiros e imprima o maior e o menor valor.

lista=[1, 5, 2, 2.000005, -5,7]
print(f'o maior é {max (lista)} e o menor é {min (lista)}')

#5. Escreva um programa que peça ao usuário para inserir seu nome e idade, e em seguida imprima uma mensagem dizendo em quantos anos ele terá 100 anos.

nome=input('diga seu nome: ')
idade=int(input('diga sua idade: '))
print(f'{nome}, faltam {100-idade} anos para você ter 100 anos')

#6. Crie uma função que receba como parâmetro um número e retorne o seu quadrado.

n=float(input('diga um número e eu o elevarei a 2: '))
print(f'esse número elevado a 2 é igual a {n**2}')

#7. Escreva um programa que verifique se um número é par ou ímpar.

n=int(input('insira um número inteiro e eu verificarei se ele é ímpar ou par: '))
if n%2==0:
	print('esse número é par')
else:
	print('esse número é impar')

#8. Crie uma lista com cinco nomes de frutas. Em seguida, peça ao usuário para inserir um nome de fruta e verifique se ela está na lista.

frutas=['maçã', 'banana', 'abacaxi', 'melancia', 'maracujá']
vrf=input('diga uma fruta e eu verificarei se ela está na lista: ')
if vrf in frutas:
	print(f'sim, "{vrf}" está na lista')
else:
	print(f'"{vrf}" não está na lista')

#9. Escreva uma função que receba uma lista de números como parâmetro e retorne a soma desses números.

list=[]
ter=float(input('diga o primeiro termo: '))
list.append(ter)
print (f'\n{list}\n')
while ter!=-0:
	ter=float(input('diga o próximo termo, ou some todos inserindo apenas "-0": '))
	if ter !=-0:
		list.append(ter)
		print (f'\naté agora a lista é: {list}\n')
else:
	print (f'\na soma dos números é {sum(list)}')

#10. Crie um programa que peça ao usuário para inserir um número e imprima todos os números de 0 até esse número.

a=int(input('diga um número inteiro e contarei de 0 até ele: '))
b=list(range(a+1))
print(b)

#11. Escreva um programa que gere uma lista de números pares de 0 a 20 e imprima essa lista.

print(list(range(0,21,2)))

#12. Crie uma função que receba como parâmetro uma lista de palavras e retorne a quantidade de palavras que começam com a letra "a".

lista=[input('digite a lista de palavras: ')]


#13. Escreva um programa que leia um número inteiro positivo e imprima todos os seus divisores.




#14. Crie uma função que receba como parâmetro um número e verifique se ele é primo.



#15. Escreva um programa que leia uma lista de números e imprima apenas os números pares.



#16. Crie uma função que receba uma lista de strings como parâmetro e retorne a lista invertida.

lista=[]
ad=' '
while ad!='':
	ad=input('diga algo para adicionar a lista de palavras, se quiser terminar re inverter as palavras apenas dê enter: ')
	if ad !='':
		lista.append(ad)
		print(f'\nlista: {lista}\n')
else:
	print(f'\na ordem invertida dessas palavras é: {lista[::-1]}')
	
#17. Escreva um programa que leia uma lista de números e remova os elementos duplicados, mantendo apenas uma ocorrência de cada número.



#18. Crie uma função que receba como parâmetro uma lista de números e retorne o produto desses números.




#19. Escreva um programa que leia uma lista de palavras e imprima somente aquelas que têm mais de cinco letras.



#20. Crie uma função que receba como parâmetro uma lista de números e retorne uma lista contendo apenas os números maiores que 10.


