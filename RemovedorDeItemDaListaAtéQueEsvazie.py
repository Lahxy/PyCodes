list=['caixa', 'feijao', 'teto', 'pao']
print (f'a lista é: {list}')
while list:
	eu=input('\ndiga o que voce quer tirar da lista: ')
	list.remove(eu)
	print(f'\na lista ficou: {list}')