x=int(input(('defina a quantia de número na sequência: ')))
rpt=0
lista=[0,1]
print('0\n1')
while rpt!=x:
	rpt += 1
	fib=lista[-1]+lista[-2]
	lista.append(fib)
	print(lista[-1])