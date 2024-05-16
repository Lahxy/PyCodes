#QUESTÃO 1
lista=[]
eu=0
while eu!=4:
	eu=int(input('''diga oque você quer fazer, digite:
1-Para adicionar um registro
2-Para remover um registro
3-Ver a lista
4-Encerrar

'''))
	print('')
	if eu==1:
		nome=input('diga o nome: ')
		numero=input('diga o número: ')
		registro=nome+': '+numero
		lista.append(registro)
		print(f'a lista ficou como {lista}\n')
	if eu==2:
		print(f'a lista é: {lista}')
		vrf=input('diga parte do registro que você quer remover: ')
		print('')
		for i in lista:
			if vrf in i:
				lista.remove(i)
				print('a lista ficou como:', lista,'\n')
	if eu==3:
		print(lista,'\n')

#QUESTÃO 2


#QUESTÃO 3
x=int(input(('defina a quantia de número na sequência: ')))
trm1=0
trm2=1
rpt=0
while rpt!=x:
	rpt += 1
	trm2=trm1+trm2