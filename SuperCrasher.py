rpt=0
lista=[0,1]
print('0\n1')
while 2:
	fib=lista[-1]+lista[-2]
	lista.append(fib)
	print(lista)
	del lista[0]