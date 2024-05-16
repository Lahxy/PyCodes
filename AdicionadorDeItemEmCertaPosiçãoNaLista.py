list=[1, '1', 2, '2', 3, '3']
print(list)
while list:
	ter=input('diga o que aparecerá na lista: ')
	pos=int(input('diga em que posição aparecerá: '))
	list.insert(pos ,ter)
	print(list)