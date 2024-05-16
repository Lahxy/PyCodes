while True:
	n=int(input('diga o número a ser testado: '))
	contagem=0
	n2=int(n/2)
	for i in range(1,n2+1):
		if i == int(n2/5) or i==2*int(n2/5) or i==3*int(n2/5) or i==4*int(n2/5):
			print(".")
		if n%i==0:
			contagem+=1
	if contagem==1 and n!=1:
		print('esse número é primo\n')
	else:
		print('esse número não é primo\n')